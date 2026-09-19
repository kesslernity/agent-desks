# Finance and Spend Desk

Most finance drift is visible weeks before anyone looks. This desk looks, on a schedule, and writes down what changed and what it cannot explain. It is deliberately better at raising a question than answering one.

**Who owns it.** The budget holder for the cost centre in question.

**Cadence.** Three scheduled watches, plus the monthly close checklist.

## What it never decides

- Whether to pay an invoice. It flags the exception and names the approver.
- Whether a variance is acceptable. It explains the arithmetic, not the tolerance.
- Whether to renew or cancel a contract.
- Any figure that goes into a statutory filing.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 10 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

**This is more than one Copilot agent can hold.** Microsoft 365 Copilot carries at most 8 skills per agent, in Agent Builder and in the Agents Toolkit alike, and this desk lists 10. So read the table as the role's full range rather than one agent's payload: take the skills for the task in front of you, or split the desk across more than one agent. Mistral Vibe documents no such limit, so the whole list can sit in one `.agents/skills/` folder. The cap is Microsoft's and preview limits move; check your own tenant rather than this sentence.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `budget-variance-explainer` | [finance](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/finance/budget-variance-explainer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/budget-variance-explainer) |
| `month-end-close-checklist` | [finance](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/finance/month-end-close-checklist) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/month-end-close-checklist) |
| `invoice-exception-review` | [finance](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/finance/invoice-exception-review) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/invoice-exception-review) |
| `expense-policy-precheck` | [finance](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/finance/expense-policy-precheck) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/expense-policy-precheck) |
| `cash-forecast-assumptions-sheet` | [finance](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/finance/cash-forecast-assumptions-sheet) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/cash-forecast-assumptions-sheet) |
| `capex-request-pack` | [finance](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/finance/capex-request-pack) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/capex-request-pack) |
| `purchase-order-anomaly-review` | [procurement](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/procurement/purchase-order-anomaly-review) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/purchase-order-anomaly-review) |
| `contract-renewal-radar` | [procurement](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/procurement/contract-renewal-radar) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/contract-renewal-radar) |
| `supplier-evaluation-matrix` | [procurement](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/procurement/supplier-evaluation-matrix) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/supplier-evaluation-matrix) |
| `kpi-definition-sheet` | [data-analytics](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/data-analytics/kpi-definition-sheet) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/kpi-definition-sheet) |

## Scheduled routines

On Mistral Vibe these are prompt files you attach to a scheduled task. The Copilot column names the prompt in that library's scheduled prompts README that answers the same question, and says so plainly where nothing does.

The two libraries were written separately, so the routines do not line up one for one. 2 of the 3 here have no Copilot counterpart yet. On that runtime you write the prompt yourself, or you leave the routine to a person. Better to say which than to link you to a file and let you find out.

| Routine | Mistral Vibe | Microsoft 365 Copilot |
|---|---|---|
| `spend-anomaly-watch` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/spend-anomaly-watch.md) | [10. Weekly Budget Alert Digest](https://github.com/kesslernity/awesome-microsoft-copilot-prompts/blob/main/prompts/scheduled-prompts/README.md#10-weekly-budget-alert-digest) |
| `vendor-renewal-lookahead` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/vendor-renewal-lookahead.md) | none, write your own |
| `kpi-pack-prep` | [prompt](https://github.com/kesslernity/awesome-mistral-vibe-prompts/blob/main/prompts/scheduled/kpi-pack-prep.md) | none, write your own |

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
