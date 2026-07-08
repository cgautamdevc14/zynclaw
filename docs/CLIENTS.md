# Client Configuration

Point agent clients at LiteLLM, not directly at vLLM.

## Shared Values

```text
Base URL: http://<litellm-host>:4000/v1
API key:  local-dev-key
Model:    Qwen3.6-27B
```

For a single-machine test:

```text
Base URL: http://localhost:4000/v1
API key:  local-dev-key
Model:    Qwen3.6-27B
```

## Environment Variables

Many OpenAI-compatible clients accept these:

```bash
export OPENAI_BASE_URL=http://localhost:4000/v1
export OPENAI_API_KEY=local-dev-key
export MODEL=Qwen3.6-27B
```

## Local Agent Task Pattern

Give the local model concrete work:

```markdown
Objective: Fix the failing lifecycle test.
Files: src/agents/lifecycle.py, tests/test_lifecycle.py
Acceptance: Existing behavior preserved, retry path handles timeout.
Validation: pytest tests/test_lifecycle.py
```

Avoid asking the local model to discover the project strategy from scratch.
Small, well-scoped execution tasks are where the local setup pays off fastest.
