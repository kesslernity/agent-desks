# Security and GRC Desk

Compliance work is mostly assembly: finding the evidence, noticing the policy drifted, reading the regulation twice. That is the part this desk does. The part it does not do is decide whether a control is effective, because that is a judgement someone has to own and be able to defend.

**Who owns it.** The control owner named in the register. The desk drafts for them, never instead of them.

**Cadence.** Two scheduled watches, plus whatever the audit calendar drags in.

## What it never decides

- Whether a control is effective. It gathers evidence and states what is missing.
- Whether an incident is reportable to a regulator. It drafts the impact brief and stops.
- Whether a vendor is acceptable. A screening brief is an input to a decision, not the decision.
- The residual risk rating on any register line.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 11 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

**This is more than one Copilot agent can hold.** Microsoft 365 Copilot carries at most 8 skills per agent, in Agent Builder and in the Agents Toolkit alike, and this desk lists 11. So read the table as the role's full range rather than one agent's payload: take the skills for the task in front of you, or split the desk across more than one agent. Mistral Vibe documents no such limit, so the whole list can sit in one `.agents/skills/` folder. The cap is Microsoft's and preview limits move; check your own tenant rather than this sentence.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `control-evidence-request-pack` | [security-grc](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/security-grc/control-evidence-request-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/control-evidence-request-pack) |
| `controls-gap-pack` | [risk-ethics-compliance](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/risk-ethics-compliance/controls-gap-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/controls-gap-pack) |
| `policy-gap-review` | [security-grc](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/security-grc/policy-gap-review) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/policy-gap-review) |
| `risk-register-update` | [security-grc](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/security-grc/risk-register-update) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/risk-register-update) |
| `vendor-risk-screening-brief` | [security-grc](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/security-grc/vendor-risk-screening-brief) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/vendor-risk-screening-brief) |
| `vendor-security-questionnaire-prefill` | [security-grc](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/security-grc/vendor-security-questionnaire-prefill) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/vendor-security-questionnaire-prefill) |
| `data-incident-impact-brief` | [security-grc](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/security-grc/data-incident-impact-brief) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/data-incident-impact-brief) |
| `dpia-draft-pack` | [data-privacy](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/data-privacy/dpia-draft-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/dpia-draft-pack) |
| `document-deidentification-pass` | [data-privacy](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/data-privacy/document-deidentification-pass) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/document-deidentification-pass) |
| `regulatory-change-impact-note` | [legal-contracts](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/legal-contracts/regulatory-change-impact-note) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/regulatory-change-impact-note) |
| `audit-prep-pack` | [quality-audit](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/quality-audit/audit-prep-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/audit-prep-pack) |

## Scheduled routines

On Mistral Vibe these are prompt files you attach to a scheduled task. The Copilot column names the prompt in that library's scheduled prompts README that answers the same question, and says so plainly where nothing does.

The two libraries were written separately, so the routines do not line up one for one. 2 of the 2 here have no Copilot counterpart yet. On that runtime you write the prompt yourself, or you leave the routine to a person. Better to say which than to link you to a file and let you find out.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `access-review-prep` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/access-review-prep.md) | none, write your own |
| `regulation-diff-watch` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/regulation-diff-watch.md) | none, write your own |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
