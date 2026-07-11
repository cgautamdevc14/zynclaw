# Connection Catalog

This catalog helps the team choose integrations without turning every tool on
at once.

| Connection | Use For | First Permission | Write Risk |
|------------|---------|------------------|------------|
| GitHub | Repos, issues, PRs, review handoff | Repo read, issues read | Medium |
| Slack | Team updates, reminders, digest posts | Post to one channel | Medium |
| Google Drive | Docs, Sheets, Slides, shared context | Read selected files | Medium |
| Google Calendar | Availability, meeting prep, reminders | Read calendar | Medium |
| Gmail or Outlook | Task extraction, follow-ups | Read selected mailbox | High |
| Linear | Issues, projects, engineering planning | Read workspace issues | Medium |
| Jira | Enterprise project tracking | Read project issues | Medium |
| Notion | Docs, lightweight knowledge base | Read selected pages/databases | Medium |
| HubSpot | CRM, accounts, deals, customer context | Read selected objects | High |
| MCP server | Standardized agent tools/resources | Explicit tool list | Depends on tools |
| Prometheus/Grafana | Metrics and dashboards | Read metrics | Low |

## Connection Details

### GitHub

Use for code review, repo context, issues, pull requests, and release notes.

Recommended auth:

- GitHub App for shared/team automation.
- Fine-grained personal access token only for local experiments.

Guardrail:

- Prefer issue and PR writes over direct branch writes.

### Slack

Use for team notifications, handoffs, and status summaries.

Recommended auth:

- Slack app with the narrow scopes needed.
- Incoming webhook only for simple one-channel notifications.

Guardrail:

- Start with one test channel before posting to team-wide channels.

### Google Drive And Calendar

Use for shared docs, spreadsheets, slides, and meeting context.

Recommended auth:

- OAuth for user-approved access.
- Service account with domain-wide delegation only when an admin approves
  workspace-wide automation.

Guardrail:

- Avoid broad Drive scopes when file-specific access is enough.

### Gmail Or Outlook

Use for task extraction and follow-up drafting.

Recommended auth:

- OAuth with the narrowest mailbox scopes available.

Guardrail:

- Draft messages first; do not auto-send until the workflow has been reviewed.

### Linear Or Jira

Use for issue tracking, delivery planning, project status, and backlog hygiene.

Recommended auth:

- OAuth app for team integrations.
- Personal token only for local testing.

Guardrail:

- Let agents draft issue updates before enabling direct status changes.

### Notion

Use for lightweight knowledge base pages and databases.

Recommended auth:

- Internal connection for selected workspace pages.
- OAuth for installable/public apps.

Guardrail:

- Share only the pages or databases the agent needs.

### HubSpot

Use for accounts, deals, customer prep, and sales handoff.

Recommended auth:

- Private app token for internal automation.
- OAuth for public/installable apps.

Guardrail:

- Confirm all CRM writes with a human until the workflow is proven.

### MCP Server

Use when you want standardized tools and resources exposed to agents.

Recommended auth:

- Start local.
- Expose only the tools the workflow needs.

Guardrail:

- Keep dangerous tools disabled by default.
