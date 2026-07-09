#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v promptfoo >/dev/null 2>&1; then
  cat <<'EOF'
promptfoo is not installed.

Install it with:
  npm install -g promptfoo

Then rerun:
  make eval-local
EOF
  exit 0
fi

promptfoo eval -c evals/promptfoo/local-agent-smoke.yaml
