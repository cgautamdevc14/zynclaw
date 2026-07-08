# Requirements Review

Use this gate before moving work into engineering.

## Required

- Problem statement is specific.
- Primary user is named.
- First slice is small enough to review.
- Acceptance criteria are testable.
- Non-goals are explicit.
- Analytics or success metrics are named when relevant.

## Questions To Ask

- What would make this change a failure?
- What is the smallest version that creates value?
- Which behavior must not regress?
- What needs a human decision instead of an agent guess?

## Handoff To Project

When ready, create or update the matching work item:

```bash
make scaffold WORK="short task name"
```
