# Project Delivery Desk

The reporting overhead of delivery, taken off the manager's evening. Status drafts, a RAID log that gets reviewed instead of archived, and an explanation of the slip that names the dependency rather than the person.

**Who owns it.** The project manager. The desk writes the update; the PM owns what it says.

**Cadence.** Two scheduled rollups, and one status pass per reporting cycle.

## What it never decides

- The RAG status. It proposes one from the evidence and the manager sets it.
- Whether a risk is accepted, mitigated or escalated.
- A date change. It explains the slip; rebaselining is a governance act.
- Who is accountable for a missed action.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 11 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

**This is more than one Copilot agent can hold.** Microsoft 365 Copilot carries at most 8 skills per agent, in Agent Builder and in the Agents Toolkit alike, and this desk lists 11. So read the table as the role's full range rather than one agent's payload: take the skills for the task in front of you, or split the desk across more than one agent. Mistral Vibe documents no such limit, so the whole list can sit in one `.agents/skills/` folder. The cap is Microsoft's and preview limits move; check your own tenant rather than this sentence.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `project-status-tracker` | [project-management](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/project-management/project-status-tracker) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/project-status-tracker) |
| `raid-log-review` | [project-management](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/project-management/raid-log-review) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/raid-log-review) |
| `schedule-slip-explainer` | [project-management](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/project-management/schedule-slip-explainer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/schedule-slip-explainer) |
| `sprint-review-summary` | [project-management](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/project-management/sprint-review-summary) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/sprint-review-summary) |
| `lessons-learned-synthesis` | [project-management](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/project-management/lessons-learned-synthesis) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/lessons-learned-synthesis) |
| `stakeholder-map-builder` | [project-management](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/project-management/stakeholder-map-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/stakeholder-map-builder) |
| `weekly-status-update-writer` | [writing-communication](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/writing-communication/weekly-status-update-writer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/weekly-status-update-writer) |
| `meeting-minutes-writer` | [meetings](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meetings/meeting-minutes-writer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/meeting-minutes-writer) |
| `meeting-prep-onepager` | [meetings](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meetings/meeting-prep-onepager) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/meeting-prep-onepager) |
| `transcript-to-actions` | [meetings](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meetings/transcript-to-actions) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/transcript-to-actions) |
| `project-dashboard-builder` | [dashboards-microapps](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/dashboards-microapps/project-dashboard-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/project-dashboard-builder) |

## Scheduled routines

On Mistral Vibe these are prompt files you attach to a scheduled task. The Copilot column names the prompt in that library's scheduled prompts README that answers the same question, and says so plainly where nothing does.

The two libraries were written separately, so the routines do not line up one for one. 1 of the 2 here has no Copilot counterpart yet. On that runtime you write the prompt yourself, or you leave the routine to a person. Better to say which than to link you to a file and let you find out.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `project-rollup` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/project-rollup.md) | [7. Weekly Project Status Brief](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md#7-weekly-project-status-brief) |
| `backlog-ageing-report` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/backlog-ageing-report.md) | none, write your own |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
