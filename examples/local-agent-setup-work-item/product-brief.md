# Improve Local Agent Setup - Product Brief

## Problem

New teammates need too much context to start the local inference stack and hand
work to agents safely.

## User

Engineering and QA teammates who want to run or validate local-agent workflows.

## First Slice

Make setup discoverable through Make targets, doctor checks, and clear docs.

## Non-Goals

- Replacing Clawrium.
- Automating production deployment.
- Removing human review.

## Acceptance Criteria

- A teammate can find the first setup command from the README.
- Preflight checks identify missing local dependencies.
- A task folder can capture product, project, engineering, and QA context.

## Metrics

- Time from clone to first doctor run.
- Number of failed setup attempts due to missing instructions.
