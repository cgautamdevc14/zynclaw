# Operations Runbook

This file captures the checks that prevent the common local-inference failure
modes from consuming a day of debugging.

## vLLM Startup Triage

When startup fails, search for the primary failure before reading shutdown
noise:

```bash
scripts/log_triage.sh logs/vllm.log
```

The important line is usually near `EngineCore failed to start`. Errors raised
while Python is shutting down can be downstream artifacts.

## First Command On A New Host

Run:

```bash
make setup
make doctor
```

`make setup` creates `.env` and performs the first local checks. `make doctor`
collects the remaining host and endpoint diagnostics without requiring you to
remember every command.

## NGC Image Patch

If your NGC vLLM image bundles a FastAPI version that is incompatible with the
prometheus middleware, derive a tiny patched image instead of editing the
container at runtime:

```bash
docker build -t vllm-qwen36:26.06-py3-patched -f infra/vllm/Dockerfile.ngc-patched .
```

Then point your compose file at that tag.

## Qwen Parser Settings

For Qwen3.6 XML-style tool calls:

```bash
--enable-auto-tool-choice
--tool-call-parser qwen3_xml
--reasoning-parser qwen3
```

Do not assume a parser based on the model family name. Confirm with the
calculator acceptance test.

## Model Runner V2

If you are serving Qwen3.5, Qwen3.6, MiniMax M2, or hybrid-attention models and
hit prefix-cache startup failures, make sure V2 is not forced:

```bash
unset VLLM_USE_V2_MODEL_RUNNER
```

In compose files, omit that environment variable instead of setting it to a
truthy value.

## MTP Verification

The speculative decoding flag is not enough. Check the resolved architecture in
vLLM startup logs:

```bash
grep -E "Resolved architecture|Detected MTP model|Loading drafter" logs/vllm.log
```

You want to see the MTP architecture when using a checkpoint that includes a
draft head. If the log shows the non-MTP architecture, the flag may be a no-op.

## GB10 Memory Query

On GB10 unified memory systems, discrete GPU memory queries may return `N/A`.
Use:

```bash
scripts/gb10_memory.sh
```

The script sums compute-process memory from `nvidia-smi`.

## LiteLLM Safety Setting

Keep this enabled:

```yaml
litellm_settings:
  drop_params: true
```

That setting lets clients send provider-specific reasoning knobs without
breaking the local route.
