#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <vllm-log-file>" >&2
  exit 2
fi

log_file="$1"

if [[ ! -f "$log_file" ]]; then
  echo "log file not found: $log_file" >&2
  exit 1
fi

grep -B2 -A20 -E "ERROR .*failed to start|EngineCore failed to start|_initialize_kv_caches" "$log_file" || {
  echo "no startup failure markers found"
}
