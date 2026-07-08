# Improve Local Agent Setup - Project Plan

## Owners

| Role | Owner |
|------|-------|
| Product | Team lead |
| Project | Team lead |
| Engineering | Local agent owner |
| QA | QA reviewer |
| Reviewer | Senior engineer |

## Milestones

| Slice | Scope | Exit Criteria | Status |
|-------|-------|---------------|--------|
| 1 | Setup commands and docs | `make setup` and `make doctor` documented | Done |
| 2 | Work-item operating model | Product/project/engineering/QA folders added | Done |
| 3 | CI smoke checks | Scripts compile and repo structure is validated | Done |

## Risks

- New process feels too heavy.
- Setup script hides errors instead of explaining them.
- Agent tasks still arrive without acceptance criteria.

## Mitigations

- Keep templates lightweight.
- Make doctor output explicit.
- Add GitHub issue templates for common workflows.
