#!/usr/bin/env bash
set -euo pipefail

if ! command -v nvidia-smi >/dev/null 2>&1; then
  echo "nvidia-smi not found" >&2
  exit 1
fi

nvidia-smi --query-compute-apps=used_memory --format=csv,noheader,nounits |
  awk '
    NF && $1 != "N/A" { total += $1 }
    END {
      printf "compute_process_memory_used_mib=%d\n", total
      printf "compute_process_memory_used_gib=%.2f\n", total / 1024
    }
  '
