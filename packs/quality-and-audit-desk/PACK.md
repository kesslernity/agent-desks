# Quality and Audit Desk

Quality work is documentation work, and documentation drifts. This desk watches the register, drafts the nonconformance, and prepares the audit pack. It is careful around anything that touches a safety case, because that is a place where a draft must never look like a clearance.

**Who owns it.** The quality manager, and for a document, its named custodian.

**Cadence.** One scheduled document watch, plus the audit calendar.

## What it never decides

- Whether a nonconformance is closed.
- Whether a corrective action was effective.
- Any safety authorisation. Not a permit to work, not a lockout, not a confined space entry, not a JSA sign-off, not an inspection clearance.
- The revision status of a controlled document.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 10 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `nonconformance-report-drafter` | [quality-audit](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/quality-audit/nonconformance-report-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/nonconformance-report-drafter) |
| `corrective-action-tracker` | [quality-audit](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/quality-audit/corrective-action-tracker) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/corrective-action-tracker) |
| `audit-prep-pack` | [quality-audit](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/quality-audit/audit-prep-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/audit-prep-pack) |
| `master-document-register-check` | [engineering-document-control](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/engineering-document-control/master-document-register-check) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/master-document-register-check) |
| `transmittal-drafter` | [engineering-document-control](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/engineering-document-control/transmittal-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/transmittal-drafter) |
| `management-of-change-intake` | [engineering-document-control](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/engineering-document-control/management-of-change-intake) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/management-of-change-intake) |
| `interface-register-builder` | [engineering-document-control](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/engineering-document-control/interface-register-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/interface-register-builder) |
| `sop-drafter` | [operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/operations/sop-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/sop-drafter) |
| `request-intake-triage` | [operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/operations/request-intake-triage) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/request-intake-triage) |
| `data-quality-issue-log` | [data-analytics](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/data-analytics/data-quality-issue-log) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/data-quality-issue-log) |

## Scheduled routines

On Mistral Vibe these are prompt files you attach to a scheduled task. On the Copilot side the equivalents live in one file, linked from each row.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `doc-change-watch` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/doc-change-watch.md) | [scheduled prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md) |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
