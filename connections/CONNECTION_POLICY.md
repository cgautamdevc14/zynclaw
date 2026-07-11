# Connection Policy

Connections expand what an agent can access. Treat them as part of the security
boundary.

## Rules

- Every connection has an owner.
- Every connection has a purpose.
- Start read-only when possible.
- Use the narrowest scopes that still support the workflow.
- Store credentials outside Git.
- Rotate credentials when owners change.
- Review write actions before enabling automation.

## Approval Levels

| Level | Example | Approval |
|-------|---------|----------|
| Read public data | Public docs, public repo metadata | Technical owner |
| Read private data | Internal docs, private issues, CRM records | Business owner and technical owner |
| Draft writes | Draft Slack post, draft email, draft issue comment | Workflow owner |
| Direct writes | Send email, change deal, update issue status | Business owner, technical owner, QA/security review |

## Required Before Enabling Writes

- Target system is named.
- Write action is reversible or auditable.
- Human approval path is documented.
- Failure mode is understood.
- Rollback or correction path is known.

## Never Commit

- API tokens.
- OAuth client secrets.
- Signing secrets.
- Webhook URLs.
- Service account JSON.
- Customer exports.
