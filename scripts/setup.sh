#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

BUILD_VLLM=0
START_VLLM=0
INSTALL_LITELLM=0

usage() {
  cat <<'EOF'
usage: scripts/setup.sh [options]

Creates .env if needed and checks the local setup.

Options:
  --install-litellm  Create .venv and install LiteLLM proxy dependencies.
  --build-vllm       Build the patched vLLM image.
  --start-vllm       Start the vLLM compose service.
  --all              Install LiteLLM, build vLLM, and start vLLM.
  -h, --help         Show this help.
EOF
}

info() {
  printf '[zynclaw] %s\n' "$*"
}

warn() {
  printf '[zynclaw] warning: %s\n' "$*" >&2
}

die() {
  printf '[zynclaw] error: %s\n' "$*" >&2
  exit 1
}

have() {
  command -v "$1" >/dev/null 2>&1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --install-litellm)
      INSTALL_LITELLM=1
      ;;
    --build-vllm)
      BUILD_VLLM=1
      ;;
    --start-vllm)
      START_VLLM=1
      ;;
    --all)
      INSTALL_LITELLM=1
      BUILD_VLLM=1
      START_VLLM=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "unknown option: $1"
      ;;
  esac
  shift
done

if [[ ! -f .env ]]; then
  cp .env.example .env
  info "created .env from .env.example"
else
  info ".env already exists"
fi

have python3 || die "python3 is required"
python3 -m py_compile scripts/acceptance.py
info "python checks passed"

if have docker; then
  info "docker found: $(docker --version)"
else
  warn "docker not found. Install Docker before building or starting vLLM."
fi

if docker compose version >/dev/null 2>&1; then
  info "docker compose found: $(docker compose version --short 2>/dev/null || docker compose version)"
else
  warn "docker compose plugin not found"
fi

if have nvidia-smi; then
  info "nvidia-smi found"
else
  warn "nvidia-smi not found. That is OK on a laptop, but the inference host needs NVIDIA drivers."
fi

if have litellm || [[ -x .venv/bin/litellm ]]; then
  info "LiteLLM command is available"
else
  warn "LiteLLM is not installed yet. Run: make install-litellm"
fi

if [[ "$INSTALL_LITELLM" -eq 1 ]]; then
  ./scripts/install_litellm.sh
fi

if [[ "$BUILD_VLLM" -eq 1 ]]; then
  have docker || die "docker is required for --build-vllm"
  docker build -t vllm-qwen36:26.06-py3-patched -f infra/vllm/Dockerfile.ngc-patched .
fi

if [[ "$START_VLLM" -eq 1 ]]; then
  have docker || die "docker is required for --start-vllm"
  docker compose version >/dev/null 2>&1 || die "docker compose is required for --start-vllm"
  docker compose --env-file .env -f infra/vllm/compose.example.yaml up -d
fi

cat <<'EOF'

Next commands:
  make doctor          # Check prerequisites and endpoint reachability
  make build-vllm      # Build patched vLLM image
  make start-vllm      # Start vLLM
  make litellm         # Start LiteLLM proxy in the foreground
  make acceptance      # Validate chat + tool-call behavior
EOF
