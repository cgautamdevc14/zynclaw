# Clawrium Notes

Clawrium is useful when the local-inference setup grows beyond one machine or
one long-running agent. It gives the team a control plane for agent lifecycle
management across SSH-accessible hosts.

## Suggested Role

Use Clawrium for:

- Registering agent hosts on the local network.
- Installing and starting agent runtimes.
- Rotating provider config and API keys.
- Tracking which agents are pointed at which model routes.
- Keeping local and remote agent processes reproducible.

Use LiteLLM for:

- The model-facing proxy endpoint.
- Normalizing client parameters.
- Centralizing usage logs.
- Exposing stable model aliases.

## Provider Shape

Expose the local model through LiteLLM and register that endpoint with agent
clients as an OpenAI-compatible provider:

```text
base_url: http://<litellm-host>:4000/v1
api_key: local-dev-key
model: Qwen3.6-27B
```

## Task Routing Pattern

1. Plan the work with a stronger planning model.
2. Create a task with exact file paths, behavior changes, and tests.
3. Assign execution to the local agent.
4. Validate locally.
5. Submit a draft PR for human review.

## Task Size Guidance

Good first tasks:

- Documentation updates tied to known behavior.
- Small bug fixes with an existing failing test.
- Guardrail checks at API boundaries.
- CLI validation and error handling.
- One-file refactors with clear tests.

Avoid first:

- Ambiguous product planning.
- Large architecture changes.
- Multi-package migrations.
- Security-sensitive edits without independent review.
