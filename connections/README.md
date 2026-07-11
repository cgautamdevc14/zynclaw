# Connections

Connections define the systems a local agent may read from or write to.

Use this folder to decide which tools should connect to the workflow, what
credentials are required, and what safety rules apply.

Start with:

- `QUICK_START.md`
- `CONNECTION_CATALOG.md`
- `CONNECTION_POLICY.md`
- `connections.example.json`
- `.env.connections.example`

## Check Current Connections

```bash
make connections-list
make connections-check
```

`connections-check` only looks for environment variables. It does not call
external APIs, send messages, create tickets, or read company data.

For a new request, use the `Connection request` GitHub issue form.

## Recommended First Connections

1. GitHub for code, PRs, issues, and repo review.
2. Slack for team updates and handoffs.
3. Google Drive or Notion for lightweight docs.
4. Linear or Jira for project tracking.
5. HubSpot only when sales/customer context is actually needed.

Add connections slowly. Every new connection increases what an agent can see or
change, so each one needs an owner and a permission boundary.
