# Governance

Governance keeps local-agent work useful, safe, and reviewable.

## Decision Rights

| Decision | Owner | Reviewer |
|----------|-------|----------|
| Product scope | Product | Project |
| Delivery priority | Project | Product |
| Agent task assignment | Engineering | Project |
| Code merge | Engineering | QA |
| Release readiness | QA | Product |
| Positioning | Marketing | Product |
| Sales talk track | Sales | Marketing |
| Model or parser change | Engineering | QA |
| New technology | Engineering | Project |

## Required Gates

Before agent assignment:

- Objective is clear.
- Scope and non-goals are written.
- Acceptance criteria are testable.
- Validation commands are listed.
- Reviewer is named.

Before merge:

- Human review is complete.
- Validation commands pass or failures are documented.
- QA checklist is complete.

Before launch:

- Product impact is clear.
- Marketing handoff is complete when user-facing.
- Sales handoff is complete when revenue-facing.
- Rollback or mitigation is known.

## Escalation

Escalate to a human owner when:

- The agent changes files outside scope.
- Acceptance criteria conflict.
- A secret or sensitive file is touched.
- A model/tooling change breaks validation.
- A customer-facing claim lacks proof.

## Change Control

Treat these as high-risk changes:

- `.github/workflows/*`
- `infra/*`
- `.env.example`
- `scripts/acceptance.py`
- `scripts/check_structure.py`
- `technology/STACK_DECISIONS.md`
- Security docs or scanning workflows.
