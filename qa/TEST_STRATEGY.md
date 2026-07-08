# Test Strategy

## Layers

| Layer | Purpose | Owner | Example |
|-------|---------|-------|---------|
| Stack smoke | Prove LiteLLM/vLLM route works | Engineering | `make doctor` |
| Tool-call acceptance | Prove structured tools work | Engineering | `make acceptance` |
| Unit tests | Prove small behavior | Engineering | `pytest tests/...` |
| Integration tests | Prove service boundaries | Engineering/QA | API or CLI tests |
| Manual QA | Prove user workflow | QA/Product | Checklist |

## Required Before Agent Work

```bash
make doctor
make acceptance
```

## Required Before Merge

- Task-specific tests pass.
- Acceptance checklist is complete.
- Release checklist is complete for user-facing changes.

## Test Data

Keep test data small, deterministic, and safe to commit.
