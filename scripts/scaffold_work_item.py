#!/usr/bin/env python3
"""Create a product-to-QA work item folder from templates."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates" / "work-item"
OUTPUT_DIR = ROOT / "work-items"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "work-item"


def render_template(text: str, title: str, slug: str, today: str) -> str:
    return (
        text.replace("{{TITLE}}", title)
        .replace("{{SLUG}}", slug)
        .replace("{{DATE}}", today)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Human-readable work item title")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    title = args.title.strip()
    slug = slugify(title)
    today = date.today().isoformat()
    target = OUTPUT_DIR / f"{today}-{slug}"

    if target.exists() and not args.force:
        raise SystemExit(f"work item already exists: {target}")

    target.mkdir(parents=True, exist_ok=True)

    for template in sorted(TEMPLATE_DIR.glob("*.md")):
        destination = target / template.name
        if destination.exists() and not args.force:
            raise SystemExit(f"file already exists: {destination}")
        content = render_template(template.read_text(encoding="utf-8"), title, slug, today)
        destination.write_text(content, encoding="utf-8")

    print(f"created {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
