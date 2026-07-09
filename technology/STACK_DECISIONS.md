# Stack Decisions

Use this file to capture technology decisions.

## Accepted

| Date | Technology | Decision | Owner |
|------|------------|----------|-------|
| 2026-07-08 | vLLM | Use for local model serving | Engineering |
| 2026-07-08 | LiteLLM | Use as the agent-facing proxy | Engineering |
| 2026-07-08 | Prometheus | Use for first-pass stack metrics | Engineering |

## Proposed

| Technology | Problem | Proposed Next Step |
|------------|---------|--------------------|
| promptfoo | Local-agent prompt and behavior regressions | Run local smoke evals before prompt/model changes |
| Phoenix or Langfuse | Multi-step agent trace visibility | Pick one tracing backend for a two-week trial |
| gitleaks | Prevent accidental secret leaks | Run locally and in GitHub Actions |

## Deferred

| Technology | Why Deferred |
|------------|--------------|
| Qdrant or pgvector | Add only when retrieval over private docs is needed |
| OPA | Add only when policy needs machine enforcement |
| Grafana | Add after Prometheus metrics are used regularly |

## Rejected

| Technology | Why Rejected |
|------------|--------------|
|  |  |
