# Agent Contract

Every local-agent task should include this information.

## Required Inputs

- Objective.
- Files or modules in scope.
- Files or modules out of scope.
- Acceptance criteria.
- Validation commands.
- Expected output format.
- Reviewer.

## Agent Responsibilities

- Read relevant files before editing.
- Keep changes scoped.
- Run the requested validation commands.
- Report failures with exact commands and output summary.
- Avoid unrelated refactors.

## Human Responsibilities

- Provide a concrete task.
- Review the diff.
- Decide tradeoffs.
- Approve release.

## Stop Conditions

The agent should stop and ask for human input when:

- Acceptance criteria conflict.
- Required files or services are missing.
- A requested change would touch sensitive credentials.
- The task expands beyond the named scope.
