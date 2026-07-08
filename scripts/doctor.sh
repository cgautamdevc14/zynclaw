#!/usr/bin/env bash
set -u -o pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

passes=0
warnings=0
failures=0

pass() {
  passes=$((passes + 1))
  printf '[pass] %s\n' "$*"
}

warn() {
  warnings=$((warnings + 1))
  printf '[warn] %s\n' "$*"
}

fail() {
  failures=$((failures + 1))
  printf '[fail] %s\n' "$*"
}

have() {
  command -v "$1" >/dev/null 2>&1
}

if [[ -f .env ]]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
  pass ".env found"
else
  warn ".env missing. Run: make setup"
fi

OPENAI_BASE_URL="${OPENAI_BASE_URL:-http://localhost:4000/v1}"
OPENAI_API_KEY="${OPENAI_API_KEY:-local-dev-key}"
VLLM_BASE_URL="${VLLM_BASE_URL:-http://localhost:8000}"
VLLM_OPENAI_BASE_URL="${VLLM_OPENAI_BASE_URL:-${VLLM_BASE_URL%/}/v1}"
VLLM_API_KEY="${VLLM_API_KEY:-local-vllm-key}"

if have python3; then
  pass "python3 found: $(python3 --version)"
else
  fail "python3 not found"
fi

if python3 -m py_compile scripts/acceptance.py >/dev/null 2>&1; then
  pass "acceptance.py compiles"
else
  fail "acceptance.py failed to compile"
fi

if bash -n scripts/*.sh >/dev/null 2>&1; then
  pass "shell scripts parse"
else
  fail "one or more shell scripts have syntax errors"
fi

if have docker; then
  pass "docker found: $(docker --version)"
  if docker info >/dev/null 2>&1; then
    pass "docker daemon reachable"
  else
    warn "docker is installed but the daemon is not reachable"
  fi
else
  warn "docker not found"
fi

if docker compose version >/dev/null 2>&1; then
  pass "docker compose found"
  if [[ -f .env ]] && docker compose --env-file .env -f infra/vllm/compose.example.yaml config -q >/dev/null 2>&1; then
    pass "vLLM compose config is valid"
  else
    warn "vLLM compose config could not be validated yet"
  fi
else
  warn "docker compose plugin not found"
fi

if have nvidia-smi; then
  if nvidia-smi >/dev/null 2>&1; then
    pass "nvidia-smi responds"
  else
    warn "nvidia-smi exists but did not return successfully"
  fi
else
  warn "nvidia-smi not found on this machine"
fi

if have litellm || [[ -x .venv/bin/litellm ]]; then
  pass "LiteLLM command available"
else
  warn "LiteLLM not found. Run: make install-litellm"
fi

if have curl; then
  models_url="${OPENAI_BASE_URL%/}/models"
  if curl -fsS --max-time 5 -H "Authorization: Bearer ${OPENAI_API_KEY}" "$models_url" >/dev/null 2>&1; then
    pass "OpenAI-compatible endpoint reachable: $models_url"
  else
    warn "endpoint not reachable yet: $models_url"
  fi

  vllm_health_url="${VLLM_BASE_URL%/}/health"
  if curl -fsS --max-time 5 "$vllm_health_url" >/dev/null 2>&1; then
    pass "vLLM health endpoint reachable: $vllm_health_url"
  else
    warn "vLLM health endpoint not reachable yet: $vllm_health_url"
  fi

  vllm_metrics_url="${VLLM_BASE_URL%/}/metrics"
  if curl -fsS --max-time 5 "$vllm_metrics_url" 2>/dev/null | grep -q "vllm:"; then
    pass "vLLM Prometheus metrics are present"
  else
    warn "vLLM Prometheus metrics not available yet: $vllm_metrics_url"
  fi

  litellm_metrics_url="${OPENAI_BASE_URL%/}"
  litellm_metrics_url="${litellm_metrics_url%/v1}/metrics"
  if curl -fsS --max-time 5 -H "Authorization: Bearer ${OPENAI_API_KEY}" "$litellm_metrics_url" >/dev/null 2>&1; then
    pass "LiteLLM metrics endpoint reachable: $litellm_metrics_url"
  else
    warn "LiteLLM metrics endpoint not reachable yet: $litellm_metrics_url"
  fi
else
  warn "curl not found, skipping endpoint reachability check"
fi

if [[ "$OPENAI_BASE_URL" == *":8000"* ]]; then
  warn "OPENAI_BASE_URL appears to point directly at vLLM. Prefer LiteLLM on port 4000 for agent clients."
fi

printf '\nSummary: %d passed, %d warnings, %d failures\n' "$passes" "$warnings" "$failures"

if [[ "$failures" -gt 0 ]]; then
  exit 1
fi
