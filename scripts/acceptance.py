#!/usr/bin/env python3
"""Smoke-test an OpenAI-compatible local model endpoint.

The test intentionally checks the parts that usually fail silently: structured
tool calls, raw XML leakage, and the public model alias exposed by LiteLLM.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any
from urllib import error, request


def build_payload(model: str) -> dict[str, Any]:
    return {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are validating a local coding-agent endpoint. "
                    "Use tools when they are available."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Think briefly, then call the calculator tool to compute "
                    "42 * 17. Do not answer in plain text."
                ),
            },
        ],
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "calculator",
                    "description": "Evaluate a basic arithmetic expression.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "Arithmetic expression to evaluate.",
                            }
                        },
                        "required": ["expression"],
                        "additionalProperties": False,
                    },
                },
            }
        ],
        "tool_choice": "auto",
        "temperature": 0,
    }


def post_chat(base_url: str, api_key: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    url = base_url.rstrip("/") + "/chat/completions"
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    req = request.Request(url, data=data, headers=headers, method="POST")

    try:
        with request.urlopen(req, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from {url}: {details}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Could not reach {url}: {exc.reason}") from exc

    return json.loads(body)


def validate_response(response: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    choices = response.get("choices") or []
    if not choices:
        return ["response did not include choices"]

    choice = choices[0]
    message = choice.get("message") or {}
    content = message.get("content")
    tool_calls = message.get("tool_calls") or []
    finish_reason = choice.get("finish_reason")

    if isinstance(content, str) and "<tool_call>" in content:
        errors.append("raw <tool_call> XML leaked into message.content")

    if not tool_calls:
        errors.append("message.tool_calls is empty")
    else:
        function = tool_calls[0].get("function") or {}
        if function.get("name") != "calculator":
            errors.append(f"expected calculator tool, got {function.get('name')!r}")

        arguments = function.get("arguments")
        if isinstance(arguments, str) and "42" not in arguments:
            errors.append(f"calculator arguments look wrong: {arguments!r}")

    if finish_reason not in {"tool_calls", "stop", None}:
        errors.append(f"unexpected finish_reason: {finish_reason!r}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=os.getenv("OPENAI_BASE_URL", "http://localhost:4000/v1"))
    parser.add_argument("--api-key", default=os.getenv("OPENAI_API_KEY", "local-dev-key"))
    parser.add_argument("--model", default=os.getenv("MODEL", "Qwen3.6-27B"))
    parser.add_argument("--timeout", type=int, default=int(os.getenv("ACCEPTANCE_TIMEOUT", "120")))
    parser.add_argument("--print-response", action="store_true")
    args = parser.parse_args()

    payload = build_payload(args.model)

    try:
        response = post_chat(args.base_url, args.api_key, payload, args.timeout)
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    if args.print_response:
        print(json.dumps(response, indent=2, sort_keys=True))

    errors = validate_response(response)
    if errors:
        for item in errors:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1

    choice = response["choices"][0]
    tool_call = choice["message"]["tool_calls"][0]
    print(
        "PASS: structured tool call accepted "
        f"model={args.model} finish_reason={choice.get('finish_reason')} "
        f"tool={tool_call.get('function', {}).get('name')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
