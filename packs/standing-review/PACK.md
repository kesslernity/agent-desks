# Standing Review

Every other pack in this repository produces output. This one reads it. The failure mode of an agent estate is not a dramatic error, it is a routine that stopped three weeks ago and nobody noticed, because absence produces no output to notice. This desk exists to make the silence legible. It writes nothing outside its own review, which is why it runs read only.

**Who owns it.** Whoever owns the agent estate. If nobody does, that is the first finding.

**Cadence.** Weekly, by hand, against the run logs of every other pack.

## What it never decides

- Whether a desk keeps running. It reports what stopped and who owns it.
- Whether an output was correct. It checks whether an output happened at all.
- Anything about a person's performance. A desk that stopped is an operational fact, not an appraisal.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 7 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `agent-evaluation-plan` | [meta-skills](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meta-skills/agent-evaluation-plan) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/agent-evaluation-plan) |
| `agent-instructions-red-team` | [meta-skills](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meta-skills/agent-instructions-red-team) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/agent-instructions-red-team) |
| `agent-instructions-drafter` | [meta-skills](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meta-skills/agent-instructions-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/agent-instructions-drafter) |
| `skill-file-reviewer` | [meta-skills](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meta-skills/skill-file-reviewer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/skill-file-reviewer) |
| `skills-backup-keeper` | [meta-skills](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meta-skills/skills-backup-keeper) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/skills-backup-keeper) |
| `no-delete-guardrail` | [meta-skills](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/meta-skills/no-delete-guardrail) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/no-delete-guardrail) |
| `news-monitor-digest` | [reporting-analysis](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/reporting-analysis/news-monitor-digest) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/news-monitor-digest) |

## Scheduled routines

**None.** Nothing here runs on a timer, deliberately. This desk keeps the cadence stated at the top of the page, which is a person's and not a scheduler's. Putting it on a timer would produce output nobody asked for. Not every role wants a cron.

## Agent profile

On Mistral Vibe, run this desk under the `read-only` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
