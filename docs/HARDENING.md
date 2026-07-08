# Production Hardening

This checklist turns the source notes into operational guardrails.

## Network Shape

- Agent clients talk to LiteLLM on `:4000`.
- LiteLLM talks to vLLM on `:8000`.
- Do not expose vLLM directly outside the trusted host or private network.
- Keep vLLM development endpoints disabled in production.

## Startup And Readiness

Use all three layers:

```bash
make doctor
make endpoint-probe
make acceptance
```

What each layer proves:

- `make doctor`: local prerequisites and basic reachability.
- `make endpoint-probe`: LiteLLM and vLLM `/models`, `/health`, and `/metrics`
  surfaces respond.
- `make acceptance`: a real chat completion returns structured tool calls.

## GPU Runtime

On the inference host:

```bash
make gpu-preflight
```

This checks host `nvidia-smi`, Docker daemon availability, and NVIDIA runtime
access from a container.

## Tool Calls

- Use `--enable-auto-tool-choice`.
- Use the Qwen-specific parser expected by your vLLM version.
- Keep `--reasoning-parser qwen3` enabled for Qwen reasoning output.
- Use strict tool schemas in tests: all fields required and
  `additionalProperties: false`.
- Run `make acceptance` after changing model, parser, chat template, or vLLM
  version.

## LiteLLM

- Keep `drop_params: true`.
- Prefer environment variables for secrets.
- Keep `turn_off_message_logging: true` unless the team has an explicit prompt
  logging policy.
- Keep Prometheus callbacks enabled on the shared proxy.

## Observability

Watch:

- Request success and failure rate.
- Time to first token.
- Inter-token latency.
- End-to-end latency.
- Waiting requests.
- KV cache usage.
- Prompt and generation token volume.

See [observability/README.md](../observability/README.md) for example
Prometheus configuration.

## Change Control

Require human review for:

- Parser changes.
- Model changes.
- Context length changes.
- GPU memory utilization changes.
- LiteLLM auth or logging changes.
- Any change that exposes a new network port.
