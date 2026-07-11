# Connections Quick Start

Use this when someone asks, "What should we connect next?"

## 1. Pick The Workflow

| Workflow | Best First Connection |
|----------|-----------------------|
| Code review and implementation | GitHub |
| Team notifications | Slack |
| Product docs | Google Drive or Notion |
| Sprint/project tracking | Linear or Jira |
| Sales handoff | HubSpot |
| Calendar or meeting prep | Google Calendar or Microsoft Graph |
| Standardized agent tools | MCP server |

## 2. Name The Owner

Every connection needs:

- Business owner.
- Technical owner.
- Reviewer.
- Rotation plan for credentials.

## 3. Choose Access Level

Start read-only when possible.

Allow writes only when:

- The action is reversible.
- The agent task names the target.
- A human reviewer is involved.
- Logs or audit history are available.

## 4. Add Environment Variables

Copy optional connection variables from:

```text
connections/.env.connections.example
```

into your local `.env` or secret manager.

## 5. Check Readiness

```bash
make connections-check
```

## 6. Document The Decision

Update:

```text
connections/CONNECTION_CATALOG.md
technology/STACK_DECISIONS.md
```
