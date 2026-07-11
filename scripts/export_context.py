#!/usr/bin/env python3
"""Export a compact Markdown context pack for agents or teammates."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "tmp" / "agent-context.md"

COMMON_FILES = [
    "README.md",
    "docs/ONE_PAGE_OVERVIEW.md",
    "docs/END_TO_END.md",
    "docs/GOVERNANCE.md",
    "security/AGENT_SECURITY.md",
]

ROLE_FILES = {
    "product": [
        "product/README.md",
        "product/INTAKE.md",
        "product/REQUIREMENTS_REVIEW.md",
        "prompts/product-to-project.md",
    ],
    "project": [
        "project/README.md",
        "project/DELIVERY_PLAN.md",
        "project/RISK_REGISTER.md",
        "project/STATUS_REPORT_TEMPLATE.md",
    ],
    "engineering": [
        "engineering/README.md",
        "engineering/AGENT_CONTRACT.md",
        "engineering/EXECUTION_PLAYBOOK.md",
        "engineering/CODE_REVIEW.md",
        "prompts/engineering-agent.md",
    ],
    "qa": [
        "qa/README.md",
        "qa/TEST_STRATEGY.md",
        "qa/ACCEPTANCE_CHECKLIST.md",
        "qa/RELEASE_CHECKLIST.md",
        "prompts/qa-agent.md",
    ],
    "marketing": [
        "marketing/README.md",
        "marketing/POSITIONING.md",
        "marketing/CAMPAIGN_PLAN.md",
        "marketing/LAUNCH_CHECKLIST.md",
        "prompts/marketing-agent.md",
    ],
    "sales": [
        "sales/README.md",
        "sales/ICP.md",
        "sales/SALES_PLAYBOOK.md",
        "sales/OBJECTION_HANDLING.md",
        "prompts/sales-agent.md",
    ],
    "technology": [
        "technology/README.md",
        "technology/TECHNOLOGY_ROADMAP.md",
        "technology/STACK_DECISIONS.md",
        "evals/README.md",
    ],
}


def files_for_role(role: str) -> list[str]:
    if role == "all":
        files = list(COMMON_FILES)
        for role_files in ROLE_FILES.values():
            files.extend(role_files)
        return dedupe(files)
    if role not in ROLE_FILES:
        known = ", ".join(["all", *sorted(ROLE_FILES)])
        raise SystemExit(f"unknown role {role!r}; choose one of: {known}")
    return dedupe([*COMMON_FILES, *ROLE_FILES[role]])


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def read_file(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.exists():
        raise SystemExit(f"missing context file: {relative_path}")
    return path.read_text(encoding="utf-8").strip()


def render(role: str, files: list[str]) -> str:
    generated = datetime.now().isoformat(timespec="seconds")
    sections = [
        "# Zynclaw Agent Context Pack",
        "",
        f"Role: {role}",
        f"Generated: {generated}",
        "",
        "Use this as compact context for a local agent or teammate. It is a",
        "snapshot of the operating model, not a replacement for human review.",
        "",
        "## Included Files",
        "",
    ]
    sections.extend(f"- `{item}`" for item in files)

    for item in files:
        sections.extend(
            [
                "",
                "---",
                "",
                f"## {item}",
                "",
                read_file(item),
            ]
        )
    sections.append("")
    return "\n".join(sections)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--role",
        default="all",
        help="Role to export: all, product, project, engineering, qa, marketing, sales, technology",
    )
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output Markdown file")
    args = parser.parse_args()

    role = args.role.strip().lower()
    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)

    files = files_for_role(role)
    output.write_text(render(role, files), encoding="utf-8")
    print(f"created {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
