#!/usr/bin/env bash
set -u -o pipefail

check() {
  local name="$1"
  local command="$2"

  if command -v "$command" >/dev/null 2>&1; then
    printf '[pass] %s found: %s\n' "$name" "$(command -v "$command")"
  else
    printf '[info] %s not installed\n' "$name"
  fi
}

check "promptfoo" "promptfoo"
check "gitleaks" "gitleaks"
check "trivy" "trivy"
check "scorecard" "scorecard"
check "node" "node"
check "npm" "npm"

cat <<'EOF'

Recommended next installs:
  npm install -g promptfoo
  brew install gitleaks
  # or use the install method from https://github.com/gitleaks/gitleaks

Optional later:
  trivy
  scorecard
  Phoenix or Langfuse for tracing
EOF
