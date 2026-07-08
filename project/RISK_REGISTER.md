# Risk Register

| Risk | Impact | Likelihood | Owner | Mitigation | Status |
|------|--------|------------|-------|------------|--------|
|  |  |  |  |  | Open |

## Common Local-Agent Risks

| Risk | Mitigation |
|------|------------|
| Agent changes too much | Give exact file scope and non-goals |
| Agent skips tests | Put validation commands in the task |
| Tool calls silently break | Run `make acceptance` before assignment |
| Review misses subtle behavior | Require QA checklist and human code review |
| Local endpoint drifts | Run `make doctor` and keep configs in Git |
