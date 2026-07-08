# Observability

This folder contains starter Prometheus config for local inference.

## What To Scrape

- LiteLLM proxy `/metrics` for request volume, latency, model aliases, teams,
  API-key aliases, and usage-related labels.
- vLLM `/metrics` for engine health, request latency, TTFT, inter-token
  latency, queue depth, token volume, and KV cache pressure.

## Local Prometheus Example

```bash
prometheus --config.file=observability/prometheus/prometheus.yml
```

The example assumes Prometheus can reach the host network on:

- `localhost:4000` for LiteLLM.
- `localhost:8000` for vLLM.

If Prometheus runs in a container, adjust targets for your Docker networking.

## Alerting Philosophy

Start with symptoms that users feel:

- High request failure rate.
- High end-to-end latency.
- High time to first token.
- Growing queue depth.

Then add capacity indicators:

- KV cache pressure.
- Running/waiting request saturation.
- Token throughput changes.

Keep alerts few and actionable. Dashboards can track more detail than pages.
