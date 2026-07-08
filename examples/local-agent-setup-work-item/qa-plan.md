# Improve Local Agent Setup - QA Plan

## Acceptance Checklist

- [ ] README explains the first setup command.
- [ ] `make setup` can run on a non-inference laptop.
- [ ] `make doctor` reports warnings instead of hard failing for missing GPU.
- [ ] `make lint` checks Python, shell scripts, and repo structure.
- [ ] Work-item templates cover product, project, engineering, QA, and status.

## Test Commands

```bash
make lint
make repo-check
python3 scripts/scaffold_work_item.py --help
```

## Regression Areas

- Existing acceptance harness still compiles.
- Existing setup docs still point at LiteLLM instead of vLLM.
- GitHub smoke workflow still runs on push and pull request.

## Release Recommendation

- [ ] Ship after checks pass.
