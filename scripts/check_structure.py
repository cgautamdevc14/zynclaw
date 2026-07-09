#!/usr/bin/env python3
"""Validate that the repo keeps its operating-model structure intact."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "SECURITY.md",
    "docs/END_TO_END.md",
    "docs/HARDENING.md",
    "docs/SETUP.md",
    "docs/START_HERE.md",
    "docs/SOURCES.md",
    "docs/VALIDATION.md",
    "evals/README.md",
    "evals/promptfoo/local-agent-smoke.yaml",
    "examples/local-agent-setup-work-item/product-brief.md",
    "marketing/README.md",
    "marketing/POSITIONING.md",
    "marketing/CAMPAIGN_PLAN.md",
    "marketing/CONTENT_PLAN.md",
    "marketing/CHANNELS.md",
    "marketing/LAUNCH_CHECKLIST.md",
    "observability/README.md",
    "observability/prometheus/prometheus.yml",
    "observability/prometheus/rules/local_inference_alerts.yml",
    "product/README.md",
    "product/INTAKE.md",
    "product/PRD_TEMPLATE.md",
    "project/README.md",
    "project/DELIVERY_PLAN.md",
    "engineering/README.md",
    "engineering/AGENT_CONTRACT.md",
    "engineering/EXECUTION_PLAYBOOK.md",
    "qa/README.md",
    "qa/TEST_STRATEGY.md",
    "qa/ACCEPTANCE_CHECKLIST.md",
    "sales/README.md",
    "sales/ICP.md",
    "sales/SALES_PLAYBOOK.md",
    "sales/OUTREACH_SEQUENCE.md",
    "sales/DEMO_SCRIPT.md",
    "sales/OBJECTION_HANDLING.md",
    "sales/QUALIFICATION.md",
    "security/README.md",
    "security/SECRETS.md",
    "security/AGENT_SECURITY.md",
    "security/SUPPLY_CHAIN.md",
    "technology/README.md",
    "technology/TECHNOLOGY_ROADMAP.md",
    "technology/STACK_DECISIONS.md",
    "templates/work-item/product-brief.md",
    "templates/work-item/project-plan.md",
    "templates/work-item/engineering-plan.md",
    "templates/work-item/marketing-plan.md",
    "templates/work-item/sales-plan.md",
    "templates/work-item/qa-plan.md",
    "templates/work-item/status.md",
    "prompts/engineering-agent.md",
    "prompts/marketing-agent.md",
    "prompts/sales-agent.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/local-agent-task.yml",
    ".github/ISSUE_TEMPLATE/marketing-request.yml",
    ".github/ISSUE_TEMPLATE/product-intake.yml",
    ".github/ISSUE_TEMPLATE/qa-report.yml",
    ".github/ISSUE_TEMPLATE/sales-enablement.yml",
    ".github/workflows/secrets.yml",
]

EXECUTABLE_SCRIPTS = [
    "scripts/acceptance.py",
    "scripts/check_structure.py",
    "scripts/doctor.sh",
    "scripts/endpoint_probe.py",
    "scripts/gb10_memory.sh",
    "scripts/gpu_preflight.sh",
    "scripts/install_litellm.sh",
    "scripts/log_triage.sh",
    "scripts/run_promptfoo_eval.sh",
    "scripts/scaffold_work_item.py",
    "scripts/setup.sh",
    "scripts/tech_doctor.sh",
]

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "#"))


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def check_required_paths() -> list[str]:
    missing = []
    for item in REQUIRED_PATHS:
        if not (ROOT / item).exists():
            missing.append(f"missing required path: {item}")
    return missing


def check_executables() -> list[str]:
    errors = []
    for item in EXECUTABLE_SCRIPTS:
        path = ROOT / item
        if not path.exists():
            errors.append(f"missing script: {item}")
        elif not os.access(path, os.X_OK):
            errors.append(f"script is not executable: {item}")
    return errors


def check_markdown_links() -> list[str]:
    errors = []
    for md_file in ROOT.rglob("*.md"):
        if ".git" in md_file.parts or ".venv" in md_file.parts:
            continue
        text = md_file.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw_target = match.group(1).strip()
            if is_external(raw_target):
                continue
            target = strip_anchor(raw_target)
            if not target:
                continue
            if target.startswith("/"):
                continue
            resolved = (md_file.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                errors.append(f"{md_file.relative_to(ROOT)} links outside repo: {raw_target}")
                continue
            if not resolved.exists():
                errors.append(f"{md_file.relative_to(ROOT)} has broken link: {raw_target}")
    return errors


def main() -> int:
    errors = []
    errors.extend(check_required_paths())
    errors.extend(check_executables())
    errors.extend(check_markdown_links())

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print("PASS: repository structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
