# Code Review Checklist

Use this when reviewing local-agent output.

## Scope

- Change matches the requested files and behavior.
- No unrelated refactor or formatting churn.
- No secrets or local machine paths were committed.

## Correctness

- Edge cases are handled.
- Error messages are clear.
- Existing behavior is preserved unless explicitly changed.
- Validation commands pass or failures are explained.

## Maintainability

- Code follows local patterns.
- New abstractions remove real complexity.
- Comments explain non-obvious decisions only.

## Tests

- Existing tests still pass.
- New behavior has targeted coverage when risk warrants it.
- Manual QA steps are documented when automated tests are not available.

## Release

- User impact is clear.
- Rollback path is known.
- Docs are updated when behavior changes.
