# Zynclaw

Local coding-agent inference stack notes, configs, and validation harnesses for a
DGX Spark style setup.

This repository turns the lessons from a working Clawrium local-inference rollout
into something a team can inspect, reuse, and extend. The goal is not to replace
frontier models for every part of engineering work. The goal is to make local
models reliable enough to execute well-scoped tasks, call tools correctly, and
survive contact with real repositories.

## Stack

- NVIDIA DGX Spark or another NVIDIA host capable of serving the model.
- Qwen3.6-27B-FP8 served through vLLM.
- LiteLLM as an OpenAI-compatible proxy, parameter normalizer, and monitoring
  point.
- Pi, Hermes, OpenCode, Continue, Cursor, or other agent clients pointed at
  LiteLLM.
- Clawrium for fleet-style lifecycle management when multiple hosts or agents
  are involved.

## Core Idea

Local inference becomes useful for engineering when the stack is treated like
production infrastructure:

1. Frontier model plans the work.
2. Local model executes the concrete task.
3. Validation harness checks chat, reasoning, tool calls, and repo tests.
4. Human review decides what ships.

That split keeps the local model in the part of the workflow where it can be
strong today: applying precise changes, using tools, and running tests once the
acceptance criteria are already clear.

## Repository Layout

```text
.
|-- docs/
|   |-- ARCHITECTURE.md
|   |-- CLAWRIUM.md
|   |-- OPERATIONS.md
|   |-- TEAM_ROLLOUT.md
|   `-- VALIDATION.md
|-- infra/
|   |-- litellm/
|   |   `-- config.example.yaml
|   `-- vllm/
|       |-- Dockerfile.ngc-patched
|       `-- compose.example.yaml
|-- scripts/
|   |-- acceptance.py
|   |-- gb10_memory.sh
|   `-- log_triage.sh
|-- .env.example
|-- LICENSE
`-- Makefile
```

## Quickstart

1. Copy the environment template.

```bash
cp .env.example .env
```

2. Build the patched vLLM image if your NGC image has the FastAPI and
   prometheus-fastapi-instrumentator mismatch.

```bash
docker build -t vllm-qwen36:26.06-py3-patched -f infra/vllm/Dockerfile.ngc-patched .
```

3. Start vLLM and LiteLLM using the examples under `infra/`.

```bash
docker compose -f infra/vllm/compose.example.yaml up -d
litellm --config infra/litellm/config.example.yaml --port 4000
```

4. Run the acceptance harness before wiring agents to the proxy.

```bash
OPENAI_BASE_URL=http://localhost:4000/v1 \
OPENAI_API_KEY=local-dev-key \
MODEL=Qwen3.6-27B \
python3 scripts/acceptance.py
```

The harness fails fast if the model returns raw tool XML in `content`, misses
`tool_calls`, or returns the wrong tool name.

## What To Validate First

- vLLM starts cleanly and the real error is not hidden behind Python shutdown
  noise.
- The Qwen tool parser is set to `qwen3_xml`, not `hermes`, for Qwen3.6 XML tool
  emission.
- Reasoning is parsed with `qwen3` so `<think>` content does not leak into the
  assistant `content` field.
- MTP is actually active by checking startup logs for the resolved architecture.
- LiteLLM has `drop_params: true` so clients with different reasoning knobs do
  not trigger avoidable 400s.

## References

- [Clawrium](https://github.com/ric03uec/clawrium): agent fleet management for
  local networks.
- [Owning Inference - Qwen3.6 on DGX Spark for real coding](https://www.devashish.me/p/owning-inference-qwen36-on-dgx-spark):
  rollout notes that inspired this repo.

## License

MIT
