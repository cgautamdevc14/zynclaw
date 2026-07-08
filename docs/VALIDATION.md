# Validation

The validation harness is the difference between an impressive demo and a stack
that can do useful engineering work.

## Acceptance Tests

Run the preflight doctor before giving the endpoint to any agent:

```bash
make doctor
```

Then run the acceptance harness:

```bash
make acceptance
```

The script checks that:

- The endpoint accepts a chat completion request.
- The model emits a structured `tool_calls` entry.
- The first tool call is named `calculator`.
- Raw `<tool_call>` XML does not leak into `message.content`.
- `finish_reason` is either `tool_calls` or another explicit value reported by
  the server.

## What A Passing Tool Call Looks Like

```json
{
  "content": null,
  "tool_calls": [
    {
      "type": "function",
      "function": {
        "name": "calculator",
        "arguments": "{\"expression\":\"42 * 17\"}"
      }
    }
  ],
  "finish_reason": "tool_calls"
}
```

## Failure Modes

### Tool Call Is In Content

Symptom:

```json
{
  "content": "<tool_call><function=calculator>...</function></tool_call>",
  "tool_calls": null
}
```

Likely cause: the vLLM tool parser does not match the model emission format.
For Qwen3.6 XML output, use `--tool-call-parser qwen3_xml`.

### Reasoning Leaks Into Content

Symptom: `<think>` appears in `message.content`.

Likely cause: reasoning parsing is not enabled or the wrong parser is selected.
For Qwen reasoning tags, use `--reasoning-parser qwen3`.

### Client Gets HTTP 400

Symptom: LiteLLM rejects a request that includes `reasoning_effort`, `thinking`,
or another provider-specific parameter.

Likely cause: `drop_params` is disabled. Add this to LiteLLM:

```yaml
litellm_settings:
  drop_params: true
```

### vLLM Health Is Green But Agents Fail

Likely cause: the health endpoint only proves that the server is up. It does
not prove that structured output, reasoning, and client parameters work
together. Run `scripts/acceptance.py` against LiteLLM, not only against vLLM.

## Repository-Level Validation

Local agents should only be assigned tasks with explicit validation commands.
Good examples:

```bash
pytest tests/test_agent_lifecycle.py
ruff check src tests
python -m compileall src
```

Avoid vague instructions such as "make this better" or "clean this up". Local
models perform best when the plan names the files, expected behavior, and test
commands.
