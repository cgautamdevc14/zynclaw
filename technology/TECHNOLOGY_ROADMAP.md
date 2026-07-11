# Technology Roadmap

This roadmap keeps the stack practical. Add technology only when it solves a
clear operating problem.

## Already In The Repo

| Area | Technology | Why It Exists |
|------|------------|---------------|
| Local serving | vLLM | Serves the local model behind an OpenAI-compatible API |
| Proxy | LiteLLM | Gives agents one stable endpoint with parameter handling and metrics |
| Stack metrics | Prometheus | Scrapes LiteLLM and vLLM metrics |
| Team workflow | GitHub issue forms | Creates structured intake for product, agent tasks, QA, marketing, and sales |
| Validation | Python and shell scripts | Checks readiness, tool calls, GPU access, and repo structure |
| Connections | Connection catalog and checker | Shows optional tool integrations and required env vars |

## Add Next

### 1. LLM Evals

Recommended starting technology: `promptfoo`.

Why:

- It can evaluate prompts, models, RAG flows, and agents.
- It can run locally or in CI.
- It supports red-team style checks when the agent workflow gets more mature.

Repo support:

- `evals/README.md`
- `evals/promptfoo/local-agent-smoke.yaml`
- `make eval-local`

Use it when:

- Changing prompts.
- Comparing local model versions.
- Testing whether the local model follows task format.
- Catching regressions before assigning real work.

### 2. LLM Tracing And Human Feedback

Recommended options:

- Phoenix when the team wants local tracing, debugging, and eval iteration.
- Langfuse when the team wants observability plus prompt management,
  experiments, and human annotation workflows.

Do not add both at first. Pick one tracing backend, run it for two weeks, then
decide whether the team needs more.

Use it when:

- Agents fail in ways that logs do not explain.
- You need to inspect tool calls and multi-step traces.
- You want human feedback on real model outputs.

### 3. Secret Scanning

Recommended starting technology: `gitleaks`.

Why:

- It checks commits and pull requests for leaked API keys and credentials.
- It is easy to run locally and in GitHub Actions.

Repo support:

- `security/SECRETS.md`
- `.github/workflows/secrets.yml`

### 4. Supply Chain And Container Scanning

Recommended technologies:

- OpenSSF Scorecard for repository security posture.
- Trivy for dependency, filesystem, and container image vulnerability scanning.

Add these after the repo has stable CI and someone owns reviewing the results.
Security scanners are only useful when alerts have owners.

### 5. Documentation Site

Recommended technology: MkDocs or Docusaurus.

Do this only if the repo grows past what a README plus `docs/` can handle.

### 6. Connection Runtime

Recommended approach:

- Start with documented connection readiness.
- Add one real client at a time.
- Prefer MCP servers when a connection should expose multiple tools/resources to
  agents.

Do this only after the team knows which workflow needs the connection. Do not
add live API clients just because an API exists.

## Later

| Area | Candidate | Add When |
|------|-----------|----------|
| Retrieval | Qdrant or pgvector | You need private docs available to agents |
| Policy | Open Policy Agent | You need machine-enforced rules for agent actions |
| Workflow orchestration | Temporal or Dagster | Agent work becomes multi-step and scheduled |
| Experiment tracking | MLflow or Langfuse experiments | Model/prompt comparisons become frequent |
| Dashboards | Grafana | Prometheus metrics are useful enough to visualize |

## Decision Rule

Before adding a tool, write down:

- What problem it solves.
- Who owns it.
- How it fails.
- What command proves it works.
- What signal tells us to remove it.
