# Architecture

The stack uses one local inference host and one proxy layer. Agents never talk
directly to vLLM. They talk to LiteLLM, which gives the team one place to expose
stable model names, remove unsupported client parameters, and add logging.

```text
agent client
  |
  | OpenAI-compatible chat completions
  v
LiteLLM proxy
  |
  | OpenAI-compatible upstream
  v
vLLM server on NVIDIA host
  |
  | Qwen3.6-27B-FP8
  v
local model runtime
```

## Responsibilities

### vLLM

- Owns model loading, token generation, prefix caching, reasoning parsing, tool
  call parsing, and speculative decoding.
- Should be started with the parser that matches the model output format.
- Should be monitored through startup logs and a small acceptance test, not only
  through a health endpoint.

### LiteLLM

- Exposes stable team-facing model names.
- Drops unsupported client parameters with `drop_params: true`.
- Centralizes request logs and cost-like usage accounting.
- Decouples clients from the exact vLLM route.

### Agent Harnesses

- Receive precise plans and acceptance criteria.
- Execute changes using tools.
- Run tests locally.
- Produce diffs or PRs for human review.

## Recommended Workflow

1. Use a frontier model for issue understanding and plan generation.
2. Feed the local agent a concrete plan with files, functions, and test commands.
3. Make the local agent execute one small task at a time.
4. Run repository tests and the stack acceptance harness.
5. Review the diff before merge.

## Why The Proxy Matters

Different clients send different reasoning-related parameters. One may send
`reasoning_effort`, another may send `thinking`, and another may send
`thinking_budget`. Local OpenAI-compatible servers often reject unknown
parameters unless the proxy normalizes or drops them. LiteLLM is the thin layer
that makes the endpoint survivable across clients.
