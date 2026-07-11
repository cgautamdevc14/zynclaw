#!/usr/bin/env python3
"""Check optional connection readiness from environment variables."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = ROOT / "connections" / "connections.example.json"


def load_dotenv(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def env_value(name: str, dotenv: dict[str, str]) -> str:
    return os.getenv(name) or dotenv.get(name, "")


def load_catalog(path: Path) -> list[dict[str, object]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("connections", []))


def configured(connection: dict[str, object], dotenv: dict[str, str]) -> tuple[bool, list[str]]:
    required = [str(item) for item in connection.get("required_env", [])]
    missing = [name for name in required if not env_value(name, dotenv)]
    return not missing, missing


def print_list(connections: list[dict[str, object]]) -> None:
    for item in connections:
        print(f"{item['id']}: {item['name']} - {item['use_for']}")


def print_status(connections: list[dict[str, object]], dotenv: dict[str, str]) -> int:
    failures = 0
    for item in connections:
        is_configured, missing = configured(item, dotenv)
        status = "ready" if is_configured else "missing"
        if missing:
            failures += 1
        print(f"[{status}] {item['id']} - {item['name']}")
        print(f"  use: {item['use_for']}")
        print(f"  auth: {item['auth_pattern']}")
        print(f"  first scope: {item['first_scope']}")
        if missing:
            print(f"  missing: {', '.join(missing)}")
        optional = [str(name) for name in item.get("optional_env", [])]
        present_optional = [name for name in optional if env_value(name, dotenv)]
        if present_optional:
            print(f"  optional present: {', '.join(present_optional)}")
        print()
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", default=str(DEFAULT_CATALOG), help="Connection catalog JSON")
    parser.add_argument("--env-file", default=str(ROOT / ".env"), help="Local env file to inspect")
    parser.add_argument("--list", action="store_true", help="List available connections")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when required vars are missing")
    args = parser.parse_args()

    catalog = load_catalog(Path(args.catalog))
    if args.list:
        print_list(catalog)
        return 0

    dotenv = load_dotenv(Path(args.env_file))
    failures = print_status(catalog, dotenv)
    if failures:
        print(
            "Copy needed variables from connections/.env.connections.example "
            "into .env or your secret manager."
        )
    if failures and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
