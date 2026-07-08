# Team Rollout

The practical target is to move a meaningful share of engineering execution and
project-management chores to local agents while keeping planning and final
judgment human-supervised.

## Week-One Goal

Offload about 40 percent of routine project-management execution:

- Turning issues into task checklists.
- Drafting implementation plans from accepted requirements.
- Applying small repo changes.
- Updating docs after code changes.
- Running validation commands and summarizing failures.
- Preparing draft PR descriptions.

## Operating Rules

1. Do not ask the local model to invent the plan for non-trivial work.
2. Give it the plan, file paths, acceptance criteria, and tests.
3. Keep tasks small enough that review is cheap.
4. Treat `scripts/acceptance.py` as a deployment gate for the model endpoint.
5. Treat repository tests as the shipping gate for code changes.

## Team Task Template

```markdown
## Objective

One sentence describing the change.

## Scope

- Files:
- Functions/classes:
- Non-goals:

## Acceptance Criteria

- Behavior:
- Error handling:
- Docs:

## Validation

- Command:
- Expected result:
```

## Metrics To Track

- Local tokens served per day.
- Acceptance-harness pass rate.
- Task success rate without human rework.
- PR review defects found after local execution.
- Time from concrete plan to draft PR.
- Frontier-model calls avoided.

## Graduation Criteria

Increase task size only when the stack has passed the acceptance harness, the
agent has shipped several small changes, and review feedback is mostly about
product judgment rather than basic correctness.
