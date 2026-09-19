# Sales Desk

Preparation, mostly. What to ask, what the deal is actually missing, and what the proposal skeleton looks like before anyone writes prose. Nothing here sends anything, and the qualification score is an argument, not a verdict.

**Who owns it.** The account owner. Every draft lands in their outbox, never in a customer's inbox.

**Cadence.** Two scheduled sweeps, the rest pulled ahead of a call.

## What it never decides

- Whether to bid. A requirements pack informs the bid or no-bid meeting.
- Price, discount or commercial terms.
- A forecast commit. Qualification scoring is evidence for the conversation.
- What is said to a customer. Every draft goes out under a person's name, after they have read it.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 10 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

**This is more than one Copilot agent can hold.** Microsoft 365 Copilot carries at most 8 skills per agent, in Agent Builder and in the Agents Toolkit alike, and this desk lists 10. So read the table as the role's full range rather than one agent's payload: take the skills for the task in front of you, or split the desk across more than one agent. Mistral Vibe documents no such limit, so the whole list can sit in one `.agents/skills/` folder. The cap is Microsoft's and preview limits move; check your own tenant rather than this sentence.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `discovery-call-prep` | [sales-bd](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/sales-bd/discovery-call-prep) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/discovery-call-prep) |
| `lead-qualification-scorer` | [sales-bd](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/sales-bd/lead-qualification-scorer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/lead-qualification-scorer) |
| `account-plan-builder` | [sales-bd](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/sales-bd/account-plan-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/account-plan-builder) |
| `deal-risk-review` | [sales-bd](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/sales-bd/deal-risk-review) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/deal-risk-review) |
| `proposal-skeleton` | [sales-bd](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/sales-bd/proposal-skeleton) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/proposal-skeleton) |
| `rfp-response-drafter` | [sales-bd](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/sales-bd/rfp-response-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/rfp-response-drafter) |
| `estimate-to-sow` | [sales-bd](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/sales-bd/estimate-to-sow) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/estimate-to-sow) |
| `rfp-comparison-pack` | [procurement](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/procurement/rfp-comparison-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/rfp-comparison-pack) |
| `rfp-requirements-pack` | [procurement](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/procurement/rfp-requirements-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/rfp-requirements-pack) |
| `case-study-drafter` | [marketing-communications](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/marketing-communications/case-study-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/case-study-drafter) |

## Scheduled routines

On Mistral Vibe these are prompt files you attach to a scheduled task. The Copilot column names the prompt in that library's scheduled prompts README that answers the same question, and says so plainly where nothing does.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `pipeline-hygiene-check` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/pipeline-hygiene-check.md) | [4. Weekly Pipeline Pulse](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md#4-weekly-pipeline-pulse) |
| `competitor-watch` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/competitor-watch.md) | [6. Competitive Intelligence Digest](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md#6-competitive-intelligence-digest) |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
