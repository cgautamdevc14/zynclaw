# Operating Cadence

Use this cadence once the repo is part of weekly work.

## Weekly Triage

Time: 30 minutes.

Agenda:

- Review new product intake issues.
- Move ready work into project plans.
- Pick local-agent candidates.
- Check blocked work.
- Confirm QA, marketing, and sales handoffs.

Output:

- One prioritized backlog.
- Clear owners for ready work.
- Explicit non-goals for agent tasks.

## Twice-Weekly Agent Review

Time: 20 minutes.

Agenda:

- Review agent-generated diffs.
- Check validation failures.
- Identify prompt or stack issues.
- Decide what needs human-only handling.

Output:

- Merged changes or follow-up issues.
- Updated eval cases when agents fail in repeatable ways.

## Monthly Stack Review

Time: 45 minutes.

Agenda:

- Review local tokens served.
- Review task success rate.
- Review validation and QA failures.
- Decide whether to add or remove technology.
- Update `technology/STACK_DECISIONS.md`.

Output:

- One or two concrete improvements.
- Clear owner for each technology decision.

## Metrics To Track

| Metric | Why It Matters |
|--------|----------------|
| Tasks assigned to local agents | Shows adoption |
| Tasks completed without major rework | Shows quality |
| Validation failures | Shows stack or prompt issues |
| Review defects | Shows risk |
| Time from ready task to reviewed PR | Shows throughput |
| Marketing/sales handoff completion | Shows release readiness |
