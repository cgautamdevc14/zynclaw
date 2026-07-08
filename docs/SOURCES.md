# Source Notes

This repo intentionally uses primary sources for technical operating guidance.

## vLLM

- vLLM tool calling docs:
  https://docs.vllm.ai/en/latest/features/tool_calling/
- vLLM online serving docs:
  https://docs.vllm.ai/en/stable/serving/online_serving/
- vLLM metrics design docs:
  https://docs.vllm.ai/en/stable/design/metrics/

Applied decisions:

- Keep `--enable-auto-tool-choice` and a Qwen-specific parser in the vLLM
  command.
- Use strict JSON-schema-style tool definitions in the acceptance harness.
- Probe `/health`, `/v1/models`, and `/metrics` instead of trusting process
  startup alone.
- Track TTFT, inter-token latency, E2E latency, queue depth, KV cache pressure,
  and request success metrics when the stack is under real use.

## Qwen

- Qwen function calling docs:
  https://qwen.readthedocs.io/en/latest/framework/function_call.html
- Qwen vLLM deployment docs:
  https://qwen.readthedocs.io/en/latest/deployment/vllm.html
- Qwen3 repository:
  https://github.com/QwenLM/Qwen3

Applied decisions:

- Treat Qwen function calling and thinking behavior as parser-sensitive.
- Avoid ReAct-style stopword templates for reasoning models.
- Keep a first-class acceptance test for structured tool calls.

## LiteLLM

- LiteLLM drop unsupported params:
  https://docs.litellm.ai/docs/completion/drop_params
- LiteLLM Prometheus metrics:
  https://docs.litellm.ai/docs/proxy/prometheus
- LiteLLM config settings:
  https://docs.litellm.ai/docs/proxy/config_settings

Applied decisions:

- Keep `drop_params: true` so client-specific unsupported OpenAI parameters do
  not break the route.
- Enable Prometheus callbacks in the example config.
- Disable message logging in the example config so observability does not
  accidentally collect prompt content.
- Always include streaming usage so clients can account for tokens more
  consistently.

## NVIDIA

- NVIDIA Container Toolkit install guide:
  https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html
- NVIDIA sample workload:
  https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html

Applied decisions:

- Add an explicit GPU container preflight command.
- Keep host `nvidia-smi` and container GPU access separate in diagnostics.

## Docker

- Docker Compose service docs:
  https://docs.docker.com/reference/compose-file/services/

Applied decisions:

- Add a vLLM `healthcheck` to the compose example.
- Keep readiness checks separate from container startup.

## GitHub

- GitHub issue forms docs:
  https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms

Applied decisions:

- Use structured issue forms for product intake, local-agent tasks, and QA
  reports.

## Observability And SRE

- Prometheus alerting practices:
  https://prometheus.io/docs/practices/alerting/
- Google SRE Workbook on SLO alerting:
  https://sre.google/workbook/alerting-on-slos/
- OpenTelemetry GenAI semantic conventions:
  https://github.com/open-telemetry/semantic-conventions-genai

Applied decisions:

- Alert on user-visible symptoms first: latency, error rate, and queue pressure.
- Treat SLOs and burn rate as the next step after the stack has steady traffic.
- Use common GenAI vocabulary for token, model, prompt, workflow, and tool-call
  telemetry when adding tracing later.

## Go-To-Market Workflow

Applied decisions:

- Keep marketing and sales as first-class workflow folders, not release
  afterthoughts.
- Require positioning, proof, talk tracks, and objection handling before a
  launch is considered ready.
- Keep marketing and sales work connected to the same work-item folder used by
  product, project, engineering, and QA.
