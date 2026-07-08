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
else
  warn "curl not found, skipping endpoint reachability check"
fi

printf '\nSummary: %d passed, %d warnings, %d failures\n' "$passes" "$warnings" "$failures"

if [[ "$failures" -gt 0 ]]; then
  exit 1
fi
