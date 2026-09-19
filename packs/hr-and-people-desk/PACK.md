# HR and People Desk

The most sensitive desk in this repository, and the one with the tightest gate. It drafts the paperwork around people decisions and never makes one. Anything that reads like an assessment of a named individual is the paperwork, not the judgement.

**Who owns it.** The HR business partner for the population affected.

**Cadence.** Event driven. Nothing here runs on a timer, deliberately.

## What it never decides

- Any outcome for a named person: hiring, rating, promotion, pay or exit.
- Whether conduct has occurred, or how it should be treated.
- Whether a policy applies to a specific case. It states what the policy says and routes the question.
- Anything that would be an employment decision under local law.

The gate that goes with this, and what a person puts their name to, is in [GATE.md](GATE.md).

## Skills, 12 of them, on either runtime

Same skill names in both libraries. Pick the runtime you are on and take the folder of that name.

**This is more than one Copilot agent can hold.** Microsoft 365 Copilot carries at most 8 skills per agent, in Agent Builder and in the Agents Toolkit alike, and this desk lists 12. So read the table as the role's full range rather than one agent's payload: take the skills for the task in front of you, or split the desk across more than one agent. Mistral Vibe documents no such limit, so the whole list can sit in one `.agents/skills/` folder. The cap is Microsoft's and preview limits move; check your own tenant rather than this sentence.

| Skill | Microsoft 365 Copilot | Mistral Vibe |
|---|---|---|
| `job-description-drafter` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/job-description-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/job-description-drafter) |
| `interview-scorecard-builder` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/interview-scorecard-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/interview-scorecard-builder) |
| `onboarding-plan-builder` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/onboarding-plan-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/onboarding-plan-builder) |
| `performance-review-drafter` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/performance-review-drafter) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/performance-review-drafter) |
| `exit-interview-synthesis` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/exit-interview-synthesis) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/exit-interview-synthesis) |
| `policy-question-answerer` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/policy-question-answerer) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/policy-question-answerer) |
| `policy-change-briefing` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/policy-change-briefing) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/policy-change-briefing) |
| `change-communication-plan` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/change-communication-plan) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/change-communication-plan) |
| `impact-log-builder` | [hr-people](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/hr-people/impact-log-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/impact-log-builder) |
| `training-needs-synthesis` | [learning-development](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/learning-development/training-needs-synthesis) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/training-needs-synthesis) |
| `course-outline-builder` | [learning-development](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/learning-development/course-outline-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/course-outline-builder) |
| `training-quiz-builder` | [learning-development](https://github.com/kesslernity/awesome-copilot-agent-skills/tree/main/skills/learning-development/training-quiz-builder) | [skill](https://github.com/kesslernity/awesome-mistral-vibe-skills/tree/main/.agents/skills/training-quiz-builder) |

## Scheduled routines

**None.** Nothing here runs on a timer, deliberately. This desk keeps the cadence stated at the top of the page, which is a person's and not a scheduler's. Putting it on a timer would produce output nobody asked for. Not every role wants a cron.

## Agent profile

On Mistral Vibe, run this desk under the `humans-decide` profile from [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents). It is the permission block, not a suggestion in the prompt.

---

<sub>Generated from `pack.toml`. Corrections go there, then run `python3 tools/build.py`.</sub>
