# Executive Desk

Two jobs. The first is the daily assembly: what moved, what is waiting on you, what you said you would do. The second is the one most decks never get, a reviewer for each function that will be in the room, run before the meeting rather than during it.

**Who owns it.** The executive whose name is on the paper.

**Cadence.** Two scheduled briefings, and the review panel on demand before anything ships.

## What it never decides

- The decision itself. A memo lays out options and a recommendation, and a person picks.
- What is disclosed to a market, a regulator or an investor.
- Whether a reviewer's objection is answered. The panel raises it; you answer it.
- Which numbers are the official ones.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 14 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

**This is more than one Copilot agent can hold.** Microsoft 365 Copilot carries at most 8 skills per agent, in Agent Builder and in the Agents Toolkit alike, and this desk lists 14. So read the table as the role's full range rather than one agent's payload: take the skills for the task in front of you, or split the desk across more than one agent. Mistral Vibe documents no such limit, so the whole list can sit in one `.agents/skills/` folder. The cap is Microsoft's and preview limits move; check your own tenant rather than this sentence.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `executive-briefing-pack` | [executive](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive/executive-briefing-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/executive-briefing-pack) |
| `board-paper-skeleton` | [executive](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive/board-paper-skeleton) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/board-paper-skeleton) |
| `decision-memo-builder` | [executive](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive/decision-memo-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/decision-memo-builder) |
| `architecture-decision-record` | [executive](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive/architecture-decision-record) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/architecture-decision-record) |
| `custom-daily-brief` | [daily-briefings](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/daily-briefings/custom-daily-brief) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/custom-daily-brief) |
| `commitment-catcher` | [daily-briefings](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/daily-briefings/commitment-catcher) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/commitment-catcher) |
| `cfo-reviewer` | [executive-review](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive-review/cfo-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/cfo-reviewer) |
| `ciso-reviewer` | [executive-review](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive-review/ciso-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/ciso-reviewer) |
| `general-counsel-reviewer` | [executive-review](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive-review/general-counsel-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/general-counsel-reviewer) |
| `coo-reviewer` | [executive-review](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive-review/coo-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/coo-reviewer) |
| `works-council-reviewer` | [executive-review](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive-review/works-council-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/works-council-reviewer) |
| `frontline-skeptic-reviewer` | [executive-review](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive-review/frontline-skeptic-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/frontline-skeptic-reviewer) |
| `investor-reviewer` | [executive-review](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/executive-review/investor-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/investor-reviewer) |
| `kpi-weekly-report-writer` | [reporting-analysis](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/reporting-analysis/kpi-weekly-report-writer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/kpi-weekly-report-writer) |

## Scheduled routines

On Mistral Vibe these are prompt files you attach to a scheduled task. The Copilot column names the prompt in that library's scheduled prompts README that answers the same question, and says so plainly where nothing does.

The two libraries were written separately, so the routines do not line up one for one. 1 of the 2 here has no Copilot counterpart yet. On that runtime you write the prompt yourself, or you leave the routine to a person. Better to say which than to link you to a file and let you find out.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `kpi-pack-prep` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/kpi-pack-prep.md) | none, write your own |
| `inbox-triage-digest` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/inbox-triage-digest.md) | [1. Morning Email Briefing](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md#1-morning-email-briefing) |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
