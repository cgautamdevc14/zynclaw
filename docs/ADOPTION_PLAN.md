# Adoption Plan

Use this plan to roll Zynclaw out without overwhelming the team.

## Week 1: Make Work Clear

Goal: use the repo for planning and handoff before agents do serious work.

Actions:

- Share [START_HERE.md](START_HERE.md) with the team.
- Ask product/project/marketing/sales/QA to try one template each.
- Create 2-3 GitHub issues using the structured issue forms.
- Pick one small local-agent candidate task.

Success criteria:

- Teammates know which folder is theirs.
- At least one work item has product, project, engineering, and QA context.
- The team has one concrete improvement request.

## Week 2: Add Agent Execution

Goal: use the local stack for narrow, reviewable work.

Actions:

- Run `make doctor`, `make endpoint-probe`, and `make acceptance`.
- Use `engineering/AGENT_CONTRACT.md` for the first agent task.
- Require a human reviewer.
- Record what worked and what broke.

Success criteria:

- One agent-generated change is reviewed.
- Validation commands are recorded.
- Review feedback is captured.

## Week 3: Add QA And Go-To-Market Handoff

Goal: stop work from ending at implementation.

Actions:

- Use `qa/ACCEPTANCE_CHECKLIST.md`.
- Fill out `marketing/POSITIONING.md` for any user-facing change.
- Fill out `sales/SALES_PLAYBOOK.md` if sales needs to explain it.
- Create a `launch-handoff.md` inside the work item.

Success criteria:

- QA, marketing, and sales know when they need to be involved.
- Launch risk is visible before release.

## Week 4: Add Evals And Metrics

Goal: make the system measurable.

Actions:

- Install `promptfoo` if the team is changing prompts or models.
- Run `make eval-local` before prompt/model changes.
- Track task success rate, validation failures, and review defects.
- Update `technology/STACK_DECISIONS.md` with any new tooling decisions.

Success criteria:

- The team has a basic eval loop.
- The team knows which technology to add next, and why.
