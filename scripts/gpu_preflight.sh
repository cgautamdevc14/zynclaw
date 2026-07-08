#!/usr/bin/env bash
set -euo pipefail

info() {
  printf '[gpu] %s\n' "$*"
}

die() {
  printf '[gpu] error: %s\n' "$*" >&2
  exit 1
}

command -v nvidia-smi >/dev/null 2>&1 || die "nvidia-smi not found on host"
command -v docker >/dev/null 2>&1 || die "docker not found"

info "host GPU check"
nvidia-smi

info "docker daemon check"
docker info >/dev/null

info "container GPU check"
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi

info "GPU container preflight passed"
