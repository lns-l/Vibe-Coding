#!/usr/bin/env python3
"""Cursor hook: validate Conventional Commits on git commit (see hooks.json)."""
# Purpose: block or warn on non-conventional commit messages before shell runs commit.

from __future__ import annotations

import json
import re
import sys

PATTERN = re.compile(
    r"^(feat|fix|chore|docs|refactor|test|style|perf|ci|build|revert)"
    r"(\([^)]+\))?!?:\s.+"
)


def extract_commit_message(command: str) -> str | None:
    """Extract -m message from a git commit command string."""
    match = re.search(r'-m\s+"([^"]+)"', command)
    if match:
        return match.group(1)
    match = re.search(r"-m\s+'([^']+)'", command)
    if match:
        return match.group(1)
    single = re.search(r"-m\s+(\S+)", command)
    if single:
        return single.group(1)
    return None


def check(payload: dict) -> dict:
    cmd = payload.get("command", "")
    if "git commit" not in cmd:
        return {"allow": True}

    msg = extract_commit_message(cmd)
    if not msg:
        return {"allow": True}

    if not PATTERN.match(msg):
        return {
            "allow": False,
            "message": (
                "Invalid commit message.\n"
                "Format: type(scope)?: description\n"
                "Types: feat|fix|chore|docs|refactor|test|style|perf|ci|build|revert\n"
                f"Received: '{msg}'\n"
                "How to fix: git commit -m \"feat(scope): short description\""
            ),
        }
    return {"allow": True}


def main() -> None:
    raw = sys.stdin.read() or "{}"
    payload = json.loads(raw)
    result = check(payload)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
