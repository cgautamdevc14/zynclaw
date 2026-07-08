# Setup Guide

This is the copy-paste path for a new teammate or a fresh inference host.

## 1. Clone And Prepare

```bash
git clone https://github.com/cgautamdevc14/zynclaw.git
cd zynclaw
make setup
```

`make setup` creates `.env` from `.env.example`, checks Python, checks Docker,
and tells you what is missing.

## 2. Edit `.env`

Open `.env` and confirm the model route:

```bash
OPENAI_BASE_URL=http://localhost:4000/v1
OPENAI_API_KEY=local-dev-key
MODEL=Qwen3.6-27B
VLLM_MODEL=Qwen/Qwen3.6-27B-FP8
```

Keep `OPENAI_BASE_URL` pointed at LiteLLM, not directly at vLLM. The proxy is
where unsupported client parameters get dropped and usage logs become central.

## 3. Install LiteLLM

```bash
make install-litellm
```

This creates a local `.venv` and installs the LiteLLM proxy package there. If
your team already manages Python dependencies another way, you can skip this and
make sure `litellm` is on your `PATH`.

## 4. Build And Start vLLM

On the inference host:

```bash
make build-vllm
make start-vllm
make logs-vllm
```

Watch the logs for:

- The selected Qwen model.
- `qwen3_xml` tool parser.
- `qwen3` reasoning parser.
- MTP architecture or drafter logs if speculative decoding is enabled.

## 5. Start LiteLLM

In a second terminal:

```bash
make litellm
```

LiteLLM listens on port `4000` by default and forwards to vLLM on port `8000`.

## 6. Run The Doctor

In a third terminal:

```bash
make doctor
```

Warnings are expected before services are running. Failures should be fixed
before handing the endpoint to agents.

## 7. Run Acceptance

```bash
make acceptance
```

A passing run confirms the model can return an OpenAI-compatible structured
`tool_calls` response through LiteLLM.

For debugging:

```bash
make acceptance-print
```

## 8. Create A Work Item

When the stack is healthy, create a complete product-to-QA task folder:

```bash
make scaffold WORK="first local agent task"
```

Fill out the generated files under `work-items/` before assigning work to an
agent.

## One Command Host Setup

If the host already has Docker, NVIDIA drivers, and Python:

```bash
make setup-all
```

This installs LiteLLM locally, builds the patched vLLM image, and starts vLLM.
Start LiteLLM separately with `make litellm` so its logs stay visible.

## Common Fixes

### Docker Is Missing

Install Docker and the NVIDIA Container Toolkit on the inference host.

### LiteLLM Is Missing

Run:

```bash
make install-litellm
```

### Endpoint Is Not Reachable

Check that vLLM is listening on `8000` and LiteLLM is listening on `4000`:

```bash
make logs-vllm
curl -s http://localhost:4000/v1/models
```

### Acceptance Fails With Raw Tool XML

Check that the vLLM command includes:

```bash
--enable-auto-tool-choice
--tool-call-parser qwen3_xml
--reasoning-parser qwen3
```
