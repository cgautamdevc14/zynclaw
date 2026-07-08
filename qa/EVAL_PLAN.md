# Local Model Eval Plan

Use this to measure whether the local stack is ready for more responsibility.

## Eval Set

Create a small set of representative tasks:

- Docs update.
- One-file bug fix.
- Test addition.
- Error handling change.
- CLI behavior change.

## Scoring

| Score | Meaning |
|-------|---------|
| 0 | Failed to complete task |
| 1 | Completed with major human repair |
| 2 | Completed with minor repair |
| 3 | Completed and passed validation |

## Required Logs

- Prompt or task brief.
- Model route and version.
- Validation commands.
- Result summary.
- Human review notes.

## Promotion Rule

Increase task complexity only after several score-3 tasks in a row.
