#!/usr/bin/env python3
"""Check whether the configured LLM endpoint is usable."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

from build_site import read_simple_yaml
from generate_daily_paper import CONFIG_PATH, load_local_env, llm_settings


def main() -> int:
    load_local_env()
    config = read_simple_yaml(Path(CONFIG_PATH))
    
    # api_key, base_url, model = llm_settings(config)
    api_key = 'sk-KvKe63LjYKdco9eQHYRLkajCqlUCZEbZEWH968Fnn0ufjzCx'
    base_url = 'https://api.ikuncode.cc/v1'
    # base_url = 'https://api.ikuncode.cc/v1/chat/completions'
    # base_url = 'https://api.ikuncode.cc/v1/responses'
    
    model = 'gpt-5.2'

    if not api_key:
        print("No API key found. Set OPENAI_API_KEY in your shell, GitHub secret, or local .env.")
        return 2

    endpoint = f"{base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a concise API health-check assistant."},
            {"role": "user", "content": "Reply with exactly: ok"},
        ],
        "temperature": 0,
        "max_tokens": 8,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "PaperRadar/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            result = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        print(f"LLM check failed: {exc}")
        print(f"Endpoint: {endpoint}")
        print(f"Model: {model}")
        return 1

    content = result["choices"][0]["message"]["content"].strip()
    print("LLM check succeeded.")
    print(f"Endpoint: {endpoint}")
    print(f"Model: {model}")
    print(f"Response: {content}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
