#!/usr/bin/env python3
"""Check that the checker catches what it claims to catch.

Every rule in build.validate gets a pack that breaks it and an assertion that the
rule fires. A validator with no failing case is a validator nobody has proven runs,
and it will happily bless the thing it was written to stop.

  python3 tools/test_build.py
"""
from __future__ import annotations

import copy
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

GOOD = {
    "slug": "example-desk",
    "role": "Example Desk",
    "one_line": "A desk that exists only in this test",
    "owner": "The person who would be blamed",
    "cadence": "Never, it is a fixture",
    "summary": "A fixture pack, used to prove the validator rejects broken ones.",
    "profile": "humans-decide",
    "skills": ["ticket-triage-pack", "runbook-drafter"],
    "scheduled": ["overnight-incident-digest.md"],
    "never_decides": ["Anything at all, it is a fixture."],
    "human_signs": ["Nothing, it is a fixture."],
}

failures: list[str] = []


def case(name: str, mutate, expect: str | None) -> None:
    """Run validate on a mutated copy of GOOD and assert what comes back.

    expect is a substring that must appear in some problem, or None meaning the
    pack must validate clean.
    """
    packs = [copy.deepcopy(GOOD)]
    mutate(packs)
    problems = build.validate(packs)
    if expect is None:
        if problems:
            failures.append(f"{name}: expected clean, got {problems}")
    elif not any(expect in p for p in problems):
        failures.append(f"{name}: expected a problem containing {expect!r}, got {problems or 'none'}")
    print(("  ok   " if not failures or failures[-1].split(":")[0] != name else "  FAIL ") + name)


def drop(field):
    def f(packs):
        packs[0].pop(field, None)
    return f


print("validator")
case("a correct pack validates clean", lambda packs: None, None)
# The two libraries currently hold the same 137 names, so no fixture can be in one
# and not the other. Both indexes are still checked separately, and an unknown name
# has to be reported against both, or a future divergence would only half register.
case("an unknown skill is reported against the Copilot library",
     lambda p: p[0]["skills"].append("does-not-exist"),
     "is not in awesome-copilot-agent-skills")
case("an unknown skill is reported against the Mistral library",
     lambda p: p[0]["skills"].append("does-not-exist"),
     "is not in awesome-mistral-vibe-skills")
case("a scheduled prompt that does not exist",
     lambda p: p[0]["scheduled"].append("prompt-we-invented.md"),
     "is not in awesome-mistral-vibe-prompts")
case("an agent profile that does not exist",
     lambda p: p[0].__setitem__("profile", "does-everything"),
     "is not in awesome-mistral-vibe-agents")
case("a pack with no skills", lambda p: p[0].__setitem__("skills", []),
     "a pack with no skills is not a pack")
case("a pack that never says what it will not decide",
     lambda p: p[0].__setitem__("never_decides", []),
     "at least one thing it never decides")
case("a pack with a gate nobody signs",
     lambda p: p[0].__setitem__("human_signs", []),
     "at least one thing a person signs")
for field in ("role", "one_line", "owner", "cadence", "summary", "human_signs"):
    case(f"a pack missing '{field}'", drop(field), f"missing required field '{field}'")
case("two packs claiming the same role",
     lambda p: p.append(dict(copy.deepcopy(GOOD), slug="other-desk")),
     "collides with")


def with_map(equivalent, no_equivalent):
    """Swap in a broken scheduled map for one case.

    The map is the only claim here that no file listing can settle, so its three
    failure modes need a case each, and each case has to be able to lie about the
    map without editing the real one.
    """
    def f(packs):
        build.load_scheduled_map = lambda: (equivalent, set(no_equivalent))
    return f


_real_map = build.load_scheduled_map
case("a routine with no verdict in the scheduled map",
     with_map({}, []), "has no entry")
case("a Copilot prompt the README does not contain",
     with_map({"overnight-incident-digest.md": "99. A Prompt Nobody Wrote"}, []),
     "is not a heading")
case("a routine both mapped and declared to have no equivalent",
     with_map({"overnight-incident-digest.md": "1. Morning Email Briefing"},
              ["overnight-incident-digest.md"]),
     "both mapped and listed")
case("a map entry naming a routine that does not exist",
     with_map({"a-routine-we-invented.md": "1. Morning Email Briefing"}, []),
     "is not in awesome-mistral-vibe-prompts")
build.load_scheduled_map = _real_map

print("generator")
_pack = copy.deepcopy(GOOD)
for text, label in ((build.pack_md(_pack), "PACK.md"), (build.gate_md(_pack), "GATE.md")):
    if "—" in text or "–" in text:
        failures.append(f"{label} contains a dash the house style does not use")
    print(f"  {'ok  ' if '—' not in text else 'FAIL'}  no em dashes in generated {label}")

# The defect this replaced: every routine linked to the same README, so a row could
# promise a Copilot equivalent that the file did not contain. Both cells are checked.
_mapped = dict(copy.deepcopy(GOOD), scheduled=["project-rollup.md"])
if "#7-weekly-project-status-brief" not in build.pack_md(_mapped):
    failures.append("a mapped routine must link to its own Copilot prompt, not the file")
print("  ok    a mapped routine deep links to the prompt that matches it")

if "none, write your own" not in build.pack_md(copy.deepcopy(GOOD)):
    failures.append("a routine with no Copilot equivalent must say so in the table")
print("  ok    a routine with no equivalent says so instead of linking")

if build.heading_anchor("10. Weekly Budget Alert Digest") != "10-weekly-budget-alert-digest":
    failures.append("heading_anchor does not match GitHub's slug")
print("  ok    heading anchors match GitHub's slug rule")

_no_cron = dict(copy.deepcopy(GOOD), scheduled=[])
if "**None.**" not in build.pack_md(_no_cron):
    failures.append("a pack with no scheduled routines must say so rather than omit the section")
print("  ok    a pack with no scheduled routines still prints the section")

print("--check, end to end")
with tempfile.TemporaryDirectory() as tmp:
    clone = Path(tmp) / "repo"
    shutil.copytree(ROOT, clone, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    r = subprocess.run([sys.executable, "tools/build.py", "--check"], cwd=clone,
                       capture_output=True, text=True)
    print(f"  {'ok  ' if r.returncode == 0 else 'FAIL'}  a clean tree passes --check")
    if r.returncode != 0:
        failures.append(f"--check failed on a clean tree: {r.stdout}{r.stderr}")

    victim = clone / "packs" / "it-service-desk" / "PACK.md"
    victim.write_text(victim.read_text() + "\nedited by hand\n")
    r = subprocess.run([sys.executable, "tools/build.py", "--check"], cwd=clone,
                       capture_output=True, text=True)
    caught = r.returncode == 1 and "packs/it-service-desk/PACK.md" in r.stdout
    print(f"  {'ok  ' if caught else 'FAIL'}  --check names a generated file edited by hand")
    if not caught:
        failures.append(f"--check missed a hand-edited PACK.md: {r.stdout}{r.stderr}")

print()
if failures:
    print(f"{len(failures)} FAILED")
    for f in failures:
        print("  " + f)
    raise SystemExit(1)
print("all checks passed")
