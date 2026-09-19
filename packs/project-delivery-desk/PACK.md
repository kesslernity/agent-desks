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

On Mistral Vibe these are prompt files you attach to a scheduled task. On the Copilot side the equivalents live in one file, linked from each row.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `project-rollup` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/project-rollup.md) | [scheduled prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md) |
| `backlog-ageing-report` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/backlog-ageing-report.md) | [scheduled prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md) |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
