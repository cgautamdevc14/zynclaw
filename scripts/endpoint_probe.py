#!/usr/bin/env python3
"""Probe LiteLLM and vLLM readiness endpoints."""

from __future__ import annotations

import argparse
import os
from urllib import error, request


def fetch(url: str, api_key: str | None = None, timeout: int = 5) -> tuple[bool, str]:
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = request.Request(url, headers=headers)
    try:
        with request.urlopen(req, timeout=timeout) as response:
            body = response.read(50000).decode("utf-8", errors="replace")
        return True, body
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        return False, f"HTTP {exc.code}: {details}"
    except error.URLError as exc:
        return False, str(exc.reason)
    except TimeoutError:
        return False, "timed out"


def print_result(label: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "WARN"
    suffix = f" - {detail}" if detail else ""
    print(f"{status}: {label}{suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--openai-base-url", default=os.getenv("OPENAI_BASE_URL", "http://localhost:4000/v1"))
    parser.add_argument("--openai-api-key", default=os.getenv("OPENAI_API_KEY", "local-dev-key"))
    parser.add_argument("--vllm-base-url", default=os.getenv("VLLM_BASE_URL", "http://localhost:8000"))
    parser.add_argument("--vllm-api-key", default=os.getenv("VLLM_API_KEY", "local-vllm-key"))
    parser.add_argument("--timeout", type=int, default=5)
    parser.add_argument("--strict", action="store_true", help="Exit non-zero when any probe fails")
    args = parser.parse_args()

    failures = 0

    litellm_models = args.openai_base_url.rstrip("/") + "/models"
    ok, body = fetch(litellm_models, args.openai_api_key, args.timeout)
    print_result(f"LiteLLM models endpoint {litellm_models}", ok, body[:120] if not ok else "")
    failures += 0 if ok else 1

    litellm_metrics = args.openai_base_url.rstrip("/")
    litellm_metrics = litellm_metrics.removesuffix("/v1") + "/metrics"
    ok, body = fetch(litellm_metrics, args.openai_api_key, args.timeout)
    print_result(f"LiteLLM metrics endpoint {litellm_metrics}", ok, body[:120] if not ok else "")
    failures += 0 if ok else 1

    vllm_health = args.vllm_base_url.rstrip("/") + "/health"
    ok, body = fetch(vllm_health, timeout=args.timeout)
    print_result(f"vLLM health endpoint {vllm_health}", ok, body[:120] if not ok else "")
    failures += 0 if ok else 1

    vllm_models = args.vllm_base_url.rstrip("/") + "/v1/models"
    ok, body = fetch(vllm_models, args.vllm_api_key, args.timeout)
    print_result(f"vLLM models endpoint {vllm_models}", ok, body[:120] if not ok else "")
    failures += 0 if ok else 1

    vllm_metrics = args.vllm_base_url.rstrip("/") + "/metrics"
    ok, body = fetch(vllm_metrics, timeout=args.timeout)
    has_vllm_metrics = ok and "vllm:" in body
    print_result(f"vLLM metrics endpoint {vllm_metrics}", has_vllm_metrics, "" if has_vllm_metrics else body[:120])
    failures += 0 if has_vllm_metrics else 1

    if failures and args.strict:
        return 1
    if failures:
        print(f"\n{failures} probe(s) are not ready yet. Start vLLM and LiteLLM, then rerun.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
