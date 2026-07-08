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
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   `-- workflows/
|-- docs/
|   |-- ARCHITECTURE.md
|   |-- CLAWRIUM.md
|   |-- CLIENTS.md
|   |-- END_TO_END.md
|   |-- HARDENING.md
|   |-- OPERATIONS.md
|   |-- SETUP.md
|   |-- SOURCES.md
|   |-- TEAM_ROLLOUT.md
|   `-- VALIDATION.md
|-- engineering/
|-- examples/
|-- observability/
|-- product/
|-- project/
|-- prompts/
|-- qa/
|-- infra/
|   |-- litellm/
|   |   `-- config.example.yaml
|   `-- vllm/
|       |-- Dockerfile.ngc-patched
|       `-- compose.example.yaml
|-- scripts/
|   |-- acceptance.py
|   |-- check_structure.py
|   |-- doctor.sh
|   |-- endpoint_probe.py
|   |-- gb10_memory.sh
|   |-- gpu_preflight.sh
|   |-- install_litellm.sh
|   |-- log_triage.sh
|   `-- scaffold_work_item.py
|-- templates/
|-- work-items/
|-- .env.example
|-- LICENSE
`-- Makefile
```

## End-To-End Workflow

Use this repo as the operating model for local-agent delivery:

```text
product -> project -> engineering -> qa -> release -> learning
```

- `product/` captures the problem, requirements, non-goals, and metrics.
- `project/` turns product intent into owners, milestones, risks, and status.
- `engineering/` defines the agent execution contract and review checklist.
- `qa/` defines acceptance, evals, regression checks, and release gates.
- `templates/` and `work-items/` keep real tasks organized end to end.
- `prompts/` contains reusable prompts for product, engineering, and QA agents.
- `examples/` shows a filled work item so the team can copy the pattern.

Create a complete work item folder with:

```bash
make scaffold WORK="improve local agent setup"
```

For the full process, see [docs/END_TO_END.md](docs/END_TO_END.md).

## Quickstart

For a fresh host:

```bash
git clone https://github.com/cgautamdevc14/zynclaw.git
cd zynclaw
make setup
```

Then follow the guided path:

```bash
make install-litellm
make build-vllm
make start-vllm
```

Start LiteLLM in a second terminal:

```bash
make litellm
```

Check the setup and run acceptance:

```bash
make doctor
make acceptance
```

The harness fails fast if the model returns raw tool XML in `content`, misses
`tool_calls`, or returns the wrong tool name.

For the detailed copy-paste guide, see [docs/SETUP.md](docs/SETUP.md).

## Make Targets

```text
make setup            Create .env and check the local machine.
make setup-all        Install LiteLLM, build vLLM, and start vLLM.
make doctor           Diagnose prerequisites and endpoint reachability.
make install-litellm  Install LiteLLM into .venv.
make build-vllm       Build the patched vLLM image.
make start-vllm       Start the vLLM compose service.
make logs-vllm        Follow vLLM logs.
make litellm          Start LiteLLM in the foreground.
make acceptance       Validate structured tool-call behavior.
make endpoint-probe   Probe LiteLLM and vLLM health, models, and metrics.
make gpu-preflight    Verify host and container GPU access.
make scaffold         Create a product/project/engineering/QA work item.
make repo-check       Validate repo structure and local Markdown links.
```

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
- `/health`, `/v1/models`, and `/metrics` are reachable where expected.
- GPU access works from both the host and an NVIDIA-enabled container.

## Hardening And Observability

- Use [docs/HARDENING.md](docs/HARDENING.md) before broad team rollout.
- Use [observability/README.md](observability/README.md) for Prometheus scrape
  and alerting examples.
- Use [docs/SOURCES.md](docs/SOURCES.md) to see which official docs informed
  the current defaults.

## Team Usage

- Use [docs/END_TO_END.md](docs/END_TO_END.md) for the full product-to-QA
  operating model.
- Use [docs/CLIENTS.md](docs/CLIENTS.md) to configure local agent clients.
- Use [docs/TEAM_ROLLOUT.md](docs/TEAM_ROLLOUT.md) to decide which work should
  go to the local stack first.
- Use the GitHub issue templates for product intake, local-agent tasks, and QA
  reports.

## References

- [Clawrium](https://github.com/ric03uec/clawrium): agent fleet management for
  local networks.
- [Owning Inference - Qwen3.6 on DGX Spark for real coding](https://www.devashish.me/p/owning-inference-qwen36-on-dgx-spark):
  rollout notes that inspired this repo.

## License

MIT
