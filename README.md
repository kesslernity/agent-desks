# Agent Desks

Nine desks. Each one is a role, the skills it uses, the routines it runs on a schedule, and a
page naming exactly what a person has to sign before anything it produces counts.

Every skill referenced here exists under the same name in two libraries, one for Microsoft 365
Copilot and one for Mistral Vibe. So a pack is not written for a runtime. Pick the runtime you
are already on and take the folders of those names.

What is checked is the naming, not the behaviour. The two runtimes differ in permissions, tool
access and how they schedule things, so the same pack will not produce identical output on
both. The claim is that you do not have to redesign the desk to move it, not that the model
will answer the same way.

## The packs

<!-- generated:begin -->
| Pack | What the desk owns | Skills | Scheduled |
|---|---|---|---|
| [**Executive Desk**](packs/executive-desk/PACK.md) | Briefings, board papers, decision memos and the review panel before you send it | 14 | 2 |
| [**Finance and Spend Desk**](packs/finance-and-spend-desk/PACK.md) | Variance, close, invoice exceptions, renewals and the anomalies nobody watches | 10 | 3 |
| [**HR and People Desk**](packs/hr-and-people-desk/PACK.md) | Job descriptions, onboarding, scorecards, policy answers and change comms | 12 | none, by design |
| [**IT Service Desk**](packs/it-service-desk/PACK.md) | Tickets, incidents, access requests and the knowledge base behind them | 12 | 2 |
| [**Project Delivery Desk**](packs/project-delivery-desk/PACK.md) | Status, RAID, slippage, sprint reviews and the weekly rollup | 11 | 2 |
| [**Quality and Audit Desk**](packs/quality-and-audit-desk/PACK.md) | Nonconformances, corrective actions, audit prep and document control | 10 | 1 |
| [**Sales Desk**](packs/sales-desk/PACK.md) | Discovery prep, qualification, deal risk, proposals and pipeline hygiene | 10 | 2 |
| [**Security and GRC Desk**](packs/security-and-grc-desk/PACK.md) | Control evidence, vendor risk, policy gaps and the regulatory diff | 11 | 2 |
| [**Standing Review**](packs/standing-review/PACK.md) | Reads what the other desks produced, names what quietly stopped, brings three moves | 7 | none, by design |

**9 packs. 95 distinct skills. 12 scheduled routines.** Drawn from a Copilot library of 137 skills and a Mistral library of 137, plus 17 agent profiles and 12 scheduled prompts. Every one of the 95 skill names above exists in both skill libraries, which `tools/build.py --check` verifies against a listing pulled from the repositories rather than a number typed here.
<!-- generated:end -->

## What a pack is

A desk is the role. A pack is the folder that defines one, and there are nine of them under
`packs/`. Three files each, plus one manifest they all share at the repository root.

| File | What it holds |
|---|---|
| `pack.toml` | The whole definition. This is the only file you edit. |
| `PACK.md` | The role, the cadence, the skill table for both runtimes. |
| `GATE.md` | What a person signs, what they need in front of them, what the desk never decides. |
| `MANIFEST.json` | Every pack in one machine readable file, at the repository root. |

`PACK.md`, `GATE.md` and `MANIFEST.json` are generated. Edit the TOML and run
`python3 tools/build.py`.

## How to run one

1. Open the pack's `PACK.md` and read the skill list. Nothing is installed for you.
2. On **Microsoft 365 Copilot**, add those skills from
   [awesome-copilot-agent-skills](https://github.com/kesslernity/awesome-copilot-agent-skills).
   Agent Builder was a Microsoft preview limited to Frontier tenants when this was written on
   19 September 2026, which is a rollout state that moves. Check what your own tenant has
   rather than taking that date as current. One Copilot agent carries at most eight skills,
   and every desk here except Standing Review lists more than eight, so a desk is a role map
   to choose from rather than a payload to upload whole. Each `PACK.md` says so where it
   applies. Mistral Vibe documents no such limit.
3. On **Mistral Vibe**, copy the same named folders from
   [awesome-mistral-vibe-skills](https://github.com/kesslernity/awesome-mistral-vibe-skills)
   into `.agents/skills/`, and start the session under the profile the pack names, from
   [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents).
   The profile is the permission block. An instruction in a prompt is not one.
4. For the scheduled routines, attach the prompt files from
   [awesome-mistral-vibe-prompts](https://github.com/kesslernity/awesome-mistral-vibe-prompts)
   to whatever your platform calls a scheduled task. Five of the twelve routines have a
   Copilot prompt that answers the same question, and each `PACK.md` links to that prompt by
   name. The other seven have none, and the table says so rather than sending you to a file
   to find out. The two libraries were written separately and the schedules did not line up.
   Point the
   output at a person. A schedule that writes into a ticket queue, a mailbox or a repository
   with nobody reading it first is the one configuration that defeats every gate in here, and
   nothing in this repository can stop you building it. I have not tested these against any
   particular scheduler.
5. Read `GATE.md` with the person who will be signing. If nobody will sign, the desk should not
   run.

## The rule that caps all of it

> **AI prepares, humans decide.** No pack here authorises a permit to work or a lockout, closes
> an incident, approves access, signs off an inspection, or decides anything about a named
> person. Where a desk touches a decision like that, it drafts the paperwork and stops. Every
> `GATE.md` names its own stopping point and its own signer, in that desk's words rather than
> repeating this one, and the build fails on a pack that names neither.

The gate is not a legal notice bolted to the end. It is the part of the pack that took the
longest to write, because naming what an agent must not decide is harder than listing what it
can do, and it is the part that stays true when the model changes.

## How the claims here are checked

This repository claims that every skill it names exists in both libraries. That claim is
checked, not asserted. `tools/refresh_indexes.sh` pulls the current file listing from each of
the four public repositories, and `tools/build.py --check` fails if a pack names a skill, a
scheduled prompt or an agent profile that is not in them. It also fails if a pack is missing an
owner, a cadence, or a single line saying what it never decides.

The scheduled routines are the one place where no listing can settle it, because the claim
there is that two differently named prompts do the same job. That pairing is written down once
in `tools/scheduled-map.toml` and checked from both ends: every routine a pack schedules needs
a verdict in that file, either a named Copilot prompt or an entry saying there is none, and
every prompt it names has to still be a heading in the Copilot README. A routine added without
a verdict fails the build.

```sh
sh tools/refresh_indexes.sh     # rebuild the indexes from the live repositories
python3 tools/build.py          # regenerate PACK.md, GATE.md, MANIFEST.json, this table
python3 tools/build.py --check  # fail if anything is stale or unverifiable
python3 tools/test_build.py     # check that the checker catches what it claims to catch
```

If one of those libraries renames a skill, the check breaks here. That is the point. What it
does not check is what is inside the skill. A folder of the right name passes, so the check
catches a rename or a deletion, not a rewrite.

## What this is not

Not a product, not a headcount, and not a claim that a desk replaces the person who owns it.
Each pack names an owner because a desk with no owner is an unattended process, and unattended
processes fail in two directions. The quiet one is that it stops and nobody notices. The worse
one is that it keeps running on a schedule, producing stale or wrong output that people have
started to trust. The standing review pack exists to catch both, and it is also the pack most
likely to be the one that quietly stopped.

## When it is wrong

Open an issue. Corrections get made in the pack's `pack.toml`, dated, and the generated files
follow. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Related

The four libraries these packs are assembled from. Counts are in the table above, derived from
the indexes rather than typed here.

- [awesome-copilot-agent-skills](https://github.com/kesslernity/awesome-copilot-agent-skills): the skills, in a discipline tree, for Microsoft 365 Copilot
- [awesome-mistral-vibe-skills](https://github.com/kesslernity/awesome-mistral-vibe-skills): the same skills, flattened, for Mistral Vibe
- [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents): the agent profiles, each checked against the loader
- [awesome-mistral-vibe-prompts](https://github.com/kesslernity/awesome-mistral-vibe-prompts): the prompts, for Vibe Work, scheduled tasks and Chat

---

CC BY-SA 4.0. Independent and vendor neutral. Not affiliated with, or endorsed by, Microsoft or
Mistral AI.
