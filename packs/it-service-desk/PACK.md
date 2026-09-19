# IT Service Desk

The desk that absorbs the volume: triage, the first draft of a runbook, the postmortem nobody has time to write, and the access review that gets skipped because it is tedious. Everything here produces a document a human then reads. None of it closes a ticket, grants access, or pushes a change.

**Who owns it.** The service desk lead. Not the person who built the agent.

**Cadence.** Two scheduled routines overnight, the rest pulled when a ticket lands.

## What it never decides

- Whether an access request is approved. It assembles the evidence and names who owns the decision.
- Whether a change goes ahead. A change request pack is an input to CAB, not a substitute for it.
- Root cause. A postmortem draft proposes one and marks it as unconfirmed until a person agrees.
- When an incident is closed.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 12 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

**This is more than one Copilot agent can hold.** Microsoft 365 Copilot carries at most 8 skills per agent, in Agent Builder and in the Agents Toolkit alike, and this desk lists 12. So read the table as the role's full range rather than one agent's payload: take the skills for the task in front of you, or split the desk across more than one agent. Mistral Vibe documents no such limit, so the whole list can sit in one `.agents/skills/` folder. The cap is Microsoft's and preview limits move; check your own tenant rather than this sentence.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `ticket-triage-pack` | [customer-support](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/customer-support/ticket-triage-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/ticket-triage-pack) |
| `incident-postmortem-drafter` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/incident-postmortem-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/incident-postmortem-drafter) |
| `runbook-drafter` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/runbook-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/runbook-drafter) |
| `knowledge-article-drafter` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/knowledge-article-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/knowledge-article-drafter) |
| `knowledge-base-hygiene-review` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/knowledge-base-hygiene-review) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/knowledge-base-hygiene-review) |
| `change-request-pack` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/change-request-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/change-request-pack) |
| `access-review-pack` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/access-review-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/access-review-pack) |
| `software-request-review` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/software-request-review) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/software-request-review) |
| `service-catalogue-entry` | [it-operations](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/it-operations/service-catalogue-entry) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/service-catalogue-entry) |
| `escalation-summary` | [customer-support](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/customer-support/escalation-summary) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/escalation-summary) |
| `inbox-triage` | [email-inbox](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/email-inbox/inbox-triage) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/inbox-triage) |
| `custom-daily-brief` | [daily-briefings](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/daily-briefings/custom-daily-brief) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/custom-daily-brief) |

## Scheduled routines

On Mistral Vibe these are prompt files you attach to a scheduled task. The Copilot column names the prompt in that library's scheduled prompts README that answers the same question, and says so plainly where nothing does.

The two libraries were written separately, so the routines do not line up one for one. 2 of the 2 here have no Copilot counterpart yet. On that runtime you write the prompt yourself, or you leave the routine to a person. Better to say which than to link you to a file and let you find out.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `overnight-incident-digest` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/overnight-incident-digest.md) | none, write your own |
| `access-review-prep` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/access-review-prep.md) | none, write your own |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
