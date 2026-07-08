# Execution Playbook

## 1. Prepare The Task

Use a work item folder:

```bash
make scaffold WORK="short task name"
```

Fill in:

- `product-brief.md`
- `project-plan.md`
- `engineering-plan.md`
- `qa-plan.md`

## 2. Validate The Stack

Before assigning work:

```bash
make doctor
make acceptance
```

## 3. Assign The Agent

Give the agent:

- Objective.
- File scope.
- Non-goals.
- Validation commands.
- Expected PR summary.

Use `prompts/engineering-agent.md` as the base prompt.

## 4. Review The Diff

Use `engineering/CODE_REVIEW.md`.

## 5. QA And Release

Use:

- `qa/ACCEPTANCE_CHECKLIST.md`
- `qa/RELEASE_CHECKLIST.md`

## Task Sizing

| Size | Good For Local Agent? | Guidance |
|------|------------------------|----------|
| 1 file | Yes | Ideal first task |
| 2-5 files | Yes | Provide exact tests |
| Cross-package | Maybe | Require human plan first |
| Architecture change | Not first pass | Use ADR and senior review |
