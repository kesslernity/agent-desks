#!/usr/bin/env python3
"""Regenerate every artifact in this repository from the pack.toml files.

Upstream is packs/<slug>/pack.toml. Everything else here is generated:
PACK.md and GATE.md per pack, MANIFEST.json, and the tables in README.md.
Edit a TOML, run this, commit both.

  python3 tools/build.py            rewrite the generated files
  python3 tools/build.py --check    fail if anything is out of date, for CI
"""
from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS = ROOT / "packs"
INDEX = ROOT / "tools" / "indexes"

COPILOT_SKILL = "https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills"
MISTRAL_SKILL = "https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills"
MISTRAL_SCHED = "https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled"
COPILOT_SCHED = ("https://github.com/kesslernity/awesome-microsoft-copilot-prompts"
                 "/blob/main/prompts/scheduled-prompts/README.md")

BEGIN, END = "<!-- generated:begin -->", "<!-- generated:end -->"


def para(text: str) -> str:
    """Join a TOML multi-line string back into one paragraph.

    The TOML is hand wrapped so it is readable as source. Markdown soft wraps
    anyway, and a paragraph on one line diffs a word at a time instead of a
    block at a time.
    """
    return " ".join(text.split())


def load_index(name: str) -> set[str]:
    path = INDEX / f"{name}.txt"
    if not path.exists():
        sys.exit(f"missing index {path}. Run tools/refresh_indexes.sh first.")
    return {line.strip() for line in path.read_text().splitlines() if line.strip()}


def copilot_paths() -> dict[str, str]:
    """Skill name to its discipline/skill path in the Copilot library.

    A name that appears under two disciplines would make the link ambiguous, so
    that is an error here rather than a silently wrong link in every table.
    """
    out: dict[str, str] = {}
    clashes: list[str] = []
    for path in sorted(load_index("copilot-skills")):
        name = path.rsplit("/", 1)[-1]
        if name in out:
            clashes.append(f"{name}: {out[name]} and {path}")
        out[name] = path
    if clashes:
        sys.exit("ambiguous skill names in copilot-skills.txt:\n  " + "\n  ".join(clashes))
    return out


def load_packs() -> list[dict]:
    packs = []
    for toml_path in sorted(PACKS.glob("*/pack.toml")):
        with toml_path.open("rb") as fh:
            data = tomllib.load(fh)
        data["slug"] = toml_path.parent.name
        data["dir"] = toml_path.parent
        packs.append(data)
    if not packs:
        sys.exit("no packs found")
    return packs


def validate(packs: list[dict]) -> list[str]:
    """Every assertion this repository makes about itself, checked here.

    A pack claims a skill runs on both runtimes. That claim is only true if the
    name is present in both libraries, so it is checked against both indexes
    rather than asserted in prose.
    """
    copilot, mistral = copilot_paths(), load_index("mistral-skills")
    scheduled = load_index("mistral-scheduled")
    profiles = load_index("mistral-profiles")
    problems: list[str] = []

    for p in packs:
        slug = p["slug"]
        for field in ("role", "one_line", "owner", "cadence", "summary",
                      "never_decides", "human_signs"):
            if not p.get(field):
                problems.append(f"{slug}: missing required field '{field}'")
        for name in p.get("skills", []):
            if name not in copilot:
                problems.append(f"{slug}: skill '{name}' is not in awesome-copilot-agent-skills")
            if name not in mistral:
                problems.append(f"{slug}: skill '{name}' is not in awesome-mistral-vibe-skills")
        for name in p.get("scheduled", []):
            if name not in scheduled:
                problems.append(f"{slug}: scheduled prompt '{name}' is not in awesome-mistral-vibe-prompts")
        if p.get("profile") and p["profile"] not in profiles:
            problems.append(f"{slug}: profile '{p['profile']}' is not in awesome-mistral-vibe-agents")
        if not p.get("skills"):
            problems.append(f"{slug}: a pack with no skills is not a pack")
        if len(p.get("never_decides", [])) < 1:
            problems.append(f"{slug}: every pack must name at least one thing it never decides")
        if len(p.get("human_signs", [])) < 1:
            problems.append(f"{slug}: every pack must name at least one thing a person signs")

    seen: dict[str, str] = {}
    for p in packs:
        role = p.get("role")
        if not role:
            continue  # already reported above as a missing field
        if role in seen:
            problems.append(f"{p['slug']}: role '{role}' collides with {seen[role]}")
        seen[role] = p["slug"]
    return problems


# Microsoft 365 Copilot carries at most eight skills per agent, in Agent Builder and the
# Agents Toolkit alike. Sourced from awesome-copilot-agent-skills (docs/SETUP-GUIDE.md and
# FAQ.md), which tracks the preview. It is a platform limit, not one this repo chose.
COPILOT_SKILL_CAP = 8

def pack_md(p: dict) -> str:
    L = [f"# {p['role']}", "", para(p["summary"]), "",
         f"**Who owns it.** {para(p['owner'])}", "",
         f"**Cadence.** {para(p['cadence'])}", "",
         "## What it never decides", ""]
    L += [f"- {x}" for x in p["never_decides"]]
    L += ["", "The gate that goes with this, and what a person puts their name to, is in "
              "[GATE.md](GATE.md).", "",
          f"## Skills, {len(p['skills'])} of them, on either runtime", "",
          "Same skill names in both libraries. Pick the runtime you are on and take the "
          "folder of that name.", ""]
    if len(p["skills"]) > COPILOT_SKILL_CAP:
        L += [f"**This is more than one Copilot agent can hold.** Microsoft 365 Copilot "
              f"carries at most {COPILOT_SKILL_CAP} skills per agent, in Agent Builder and "
              f"in the Agents Toolkit alike, and this desk lists {len(p['skills'])}. So read "
              f"the table as the role's full range rather than one agent's payload: take the "
              f"skills for the task in front of you, or split the desk across more than one "
              f"agent. Mistral Vibe documents no such limit, so the whole list can sit in one "
              f"`.agents/skills/` folder. The cap is Microsoft's and preview limits move; "
              f"check your own tenant rather than this sentence.", ""]
    L += ["| Skill | Microsoft 365 Copilot | Mistral Vibe |", "|---|---|---|"]
    paths = copilot_paths()
    for s in p["skills"]:
        L.append(f"| `{s}` | [{paths[s].split('/')[0]}]({COPILOT_SKILL}/{paths[s]}) "
                 f"| [skill]({MISTRAL_SKILL}/{s}) |")
    L += [""]
    if p.get("scheduled"):
        L += ["## Scheduled routines", "",
              "On Mistral Vibe these are prompt files you attach to a scheduled task. On the "
              "Copilot side the equivalents live in one file, linked from each row.", "",
              "| Routine | Mistral Vibe | Microsoft 365 Copilot |", "|---|---|---|"]
        for s in p["scheduled"]:
            L.append(f"| `{s[:-3]}` | [prompt]({MISTRAL_SCHED}/{s}) | [scheduled prompts]({COPILOT_SCHED}) |")
        L += [""]
    else:
        L += ["## Scheduled routines", "",
              "**None.** Nothing here runs on a timer, deliberately. This desk keeps the "
              "cadence stated at the top of the page, which is a person's and not a "
              "scheduler's. Putting it on a timer would produce output nobody asked for. "
              "Not every role wants a cron.", ""]
    if p.get("profile"):
        L += ["## Agent profile", "",
              f"On Mistral Vibe, run this desk under the `{p['profile']}` profile from "
              f"[awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). "
              "It is the permission block, not a suggestion in the prompt.", ""]
    L += ["---", "", "<sub>Generated from `pack.toml`. Corrections go there, then run "
          "`python3 tools/build.py`.</sub>", ""]
    return "\n".join(L)


def gate_md(p: dict) -> str:
    L = [f"# Gate: {p['role']}", "",
         "This desk prepares. A person decides. That is not a disclaimer, it is the "
         "design, and this page is where it is written down.", "",
         "## What a person signs", ""]
    L += [f"- {x}" for x in p["human_signs"]]
    L += ["", "## What the signer needs in front of them", ""]
    L += [f"- {x}" for x in p.get("evidence", [
        "The source documents the output was built from, named, not summarised.",
        "The date each source was read.",
        "Anything the desk could not find, stated as a gap rather than omitted."])]
    L += ["", "## What this desk never decides", ""]
    L += [f"- {x}" for x in p["never_decides"]]
    L += ["", "## If it is wrong", "", para(p.get("when_wrong",
          "Write down what the desk produced, what a person approved, and which of the two "
          "was wrong. A desk that is never corrected is a desk nobody is reading.")), "",
          "---", "",
          "<sub>Generated from `pack.toml`. Corrections go there, then run "
          "`python3 tools/build.py`.</sub>", ""]
    return "\n".join(L)


def readme_tables(packs: list[dict]) -> str:
    skills = sorted({s for p in packs for s in p["skills"]})
    sched = sorted({s for p in packs for s in p.get("scheduled", [])})
    L = ["| Pack | What the desk owns | Skills | Scheduled |", "|---|---|---|---|"]
    for p in packs:
        n = len(p.get("scheduled", []))
        L.append(f"| [**{p['role']}**](packs/{p['slug']}/PACK.md) | {para(p['one_line'])} "
                 f"| {len(p['skills'])} | {n if n else 'none, by design'} |")
    copilot, mistral = len(load_index("copilot-skills")), len(load_index("mistral-skills"))
    profiles, prompts = len(load_index("mistral-profiles")), len(load_index("mistral-scheduled"))
    L += ["", f"**{len(packs)} packs. {len(skills)} distinct skills. {len(sched)} scheduled "
              f"routines.** Drawn from a Copilot library of {copilot} skills and a Mistral "
              f"library of {mistral}, plus {profiles} agent profiles and {prompts} scheduled "
              f"prompts. Every one of the {len(skills)} skill names above exists in both skill "
              "libraries, which `tools/build.py --check` verifies against a listing pulled from "
              "the repositories rather than a number typed here."]
    return "\n".join(L)


def write(path: Path, text: str, check: bool, stale: list[str]) -> None:
    current = path.read_text() if path.exists() else None
    if current == text:
        return
    if check:
        stale.append(str(path.relative_to(ROOT)))
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


def main() -> int:
    check = "--check" in sys.argv
    packs = load_packs()

    problems = validate(packs)
    if problems:
        print("VALIDATION FAILED")
        for line in problems:
            print("  " + line)
        return 1

    stale: list[str] = []
    for p in packs:
        write(p["dir"] / "PACK.md", pack_md(p), check, stale)
        write(p["dir"] / "GATE.md", gate_md(p), check, stale)

    manifest = {
        "packs": [{
            "slug": p["slug"], "role": p["role"], "owner": p["owner"],
            "cadence": p["cadence"], "one_line": p["one_line"],
            "skills": p["skills"], "scheduled": p.get("scheduled", []),
            "profile": p.get("profile"), "never_decides": p["never_decides"],
        } for p in packs],
        "totals": {
            "packs": len(packs),
            "distinct_skills": len({s for p in packs for s in p["skills"]}),
            "scheduled_routines": len({s for p in packs for s in p.get("scheduled", [])}),
        },
    }
    write(ROOT / "MANIFEST.json", json.dumps(manifest, indent=2) + "\n", check, stale)

    readme = ROOT / "README.md"
    if readme.exists():
        text = readme.read_text()
        if BEGIN in text and END in text:
            head, rest = text.split(BEGIN, 1)
            _, tail = rest.split(END, 1)
            write(readme, f"{head}{BEGIN}\n{readme_tables(packs)}\n{END}{tail}", check, stale)

    if check and stale:
        print("OUT OF DATE, run python3 tools/build.py:")
        for s in stale:
            print("  " + s)
        return 1
    print(f"OK: {len(packs)} packs, "
          f"{manifest['totals']['distinct_skills']} distinct skills, "
          f"{manifest['totals']['scheduled_routines']} scheduled routines"
          + (" (check)" if check else " (written)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
