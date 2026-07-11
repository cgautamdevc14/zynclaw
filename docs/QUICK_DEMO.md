# Quick Demo

Use this 10-minute flow to show the repo to a teammate.

## 1. Start With The Plain-English Guide

Open:

```text
docs/START_HERE.md
```

Explain that non-technical teammates can use issue forms and folders without
running the model stack.

## 2. Show The Workflow

Open:

```text
docs/END_TO_END.md
```

Point to:

```text
product -> project -> engineering -> qa -> marketing/sales -> release -> learning
```

## 3. Show A Filled Example

Open:

```text
examples/local-agent-setup-work-item/
```

Show how product, project, engineering, QA, and status files connect.

## 4. Show A New Work Item

For a technical demo:

```bash
make scaffold WORK="demo launch checklist"
```

Then open the generated folder under `work-items/`.

## 5. Show The Safety Gates

Open:

```text
engineering/AGENT_CONTRACT.md
qa/ACCEPTANCE_CHECKLIST.md
security/AGENT_SECURITY.md
```

Explain that agents do execution, but humans keep ownership.

## 6. Show Connections

Open:

```text
connections/CONNECTION_CATALOG.md
connections/CONNECTION_POLICY.md
```

For a technical demo:

```bash
make connections-list
make connections-check
```

Explain that connections are added slowly, with owners, narrow scopes, and
human approval for writes.

## 7. Close With The Ask

Ask each function to try one thing:

- Product: create one intake issue.
- Project: fill one delivery plan.
- Engineering: identify one agent-safe task.
- QA: review one acceptance checklist.
- Marketing: write one positioning draft.
- Sales: add one objection and response.
