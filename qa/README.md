# QA

QA owns confidence before release.

Use this folder to define what must pass before agent-generated work ships:

- `TEST_STRATEGY.md`: test layers and ownership.
- `ACCEPTANCE_CHECKLIST.md`: task-level validation.
- `EVAL_PLAN.md`: local-model behavior evaluation.
- `RELEASE_CHECKLIST.md`: final release gate.

## QA Rules

- Test the behavior, not just the implementation.
- Validate the model endpoint before agent assignment.
- Keep manual checks explicit and repeatable.
- Do not merge when acceptance criteria are ambiguous.
