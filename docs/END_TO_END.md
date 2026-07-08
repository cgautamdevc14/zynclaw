# End-To-End Operating Model

This repo is organized around a simple path from idea to validated delivery.
Each folder owns one stage of the workflow.

```text
product -> project -> engineering -> qa -> release -> learning
```

## 1. Product Intake

Start in `product/`.

Artifacts:

- `product/INTAKE.md`
- `product/PRD_TEMPLATE.md`
- `product/METRICS.md`

Exit criteria:

- The customer problem is specific.
- Non-goals are explicit.
- Success metrics are measurable.
- The first usable slice is small enough for one implementation pass.

## 2. Project Shaping

Move to `project/`.

Artifacts:

- `project/DELIVERY_PLAN.md`
- `project/RISK_REGISTER.md`
- `project/STATUS_REPORT_TEMPLATE.md`

Exit criteria:

- Owner, reviewer, and QA owner are named.
- Dependencies are known.
- Delivery slices are ordered.
- Risks have mitigations.

## 3. Engineering Execution

Move to `engineering/`.

Artifacts:

- `engineering/AGENT_CONTRACT.md`
- `engineering/EXECUTION_PLAYBOOK.md`
- `engineering/CODE_REVIEW.md`
- `engineering/ADR_TEMPLATE.md`

Exit criteria:

- File scope is named.
- Validation commands are known.
- Agent task is narrow and reviewable.
- Human review is required before merge.

## 4. QA Validation

Move to `qa/`.

Artifacts:

- `qa/TEST_STRATEGY.md`
- `qa/ACCEPTANCE_CHECKLIST.md`
- `qa/EVAL_PLAN.md`
- `qa/RELEASE_CHECKLIST.md`

Exit criteria:

- Acceptance criteria pass.
- Regression risk is covered.
- Local model tool-call behavior still passes.
- Release notes and rollback notes are ready.

## 5. Work Item Folder

For real work, create a dedicated folder:

```bash
make scaffold WORK="improve agent setup flow"
```

This creates:

```text
work-items/YYYY-MM-DD-improve-agent-setup-flow/
|-- product-brief.md
|-- project-plan.md
|-- engineering-plan.md
|-- qa-plan.md
`-- status.md
```

That folder becomes the single source of truth for the task.

For a filled example, see `examples/local-agent-setup-work-item/`.

## Definition Of Ready

A task is ready for a local engineering agent when it has:

- Objective.
- File scope.
- Non-goals.
- Acceptance criteria.
- Validation commands.
- Reviewer.

## Definition Of Done

A task is done when:

- Code or docs are changed.
- Validation commands pass or failures are documented.
- QA checklist is complete.
- PR description names user impact and risk.
- Human review is complete.
