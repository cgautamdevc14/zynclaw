# Improve Local Agent Setup - Engineering Plan

## Objective

Make the repo easier and safer to use from clone to agent assignment.

## Scope

- `Makefile`
- `scripts/`
- `docs/`
- `product/`
- `project/`
- `engineering/`
- `qa/`
- `.github/`

## Approach

- Add guided Make targets.
- Add preflight and structure checks.
- Add operating-model folders.
- Add templates and prompts.
- Add CI smoke validation.

## Validation

```bash
make lint
make repo-check
```

## Non-Goals

- Starting a real vLLM server in CI.
- Installing GPU drivers.
- Running endpoint acceptance when no local endpoint is available.
