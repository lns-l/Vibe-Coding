#!/usr/bin/env python3
"""Cursor hook: block git commit when project linter fails (see hooks.json)."""
# Purpose: run LINT_CMD before commit shell; failClosed when linter returns non-zero.

from __future__ import annotations

import json
import os
import subprocess
import sys

# Replace with your project linter, e.g. ["npm", "run", "lint"] or ["ruff", "check", "src"]
LINT_CMD = os.getenv("CURSOR_LINT_CMD", "").split()
LINT_ENABLED = os.getenv("CURSOR_LINT_HOOK", "off") == "on"


def check(payload: dict) -> dict:
    if not LINT_ENABLED or not LINT_CMD:
        return {"allow": True}

    cmd = payload.get("command", "")
    if "git commit" not in cmd:
        return {"allow": True}

    result = subprocess.run(LINT_CMD, capture_output=True, text=True)
    if result.returncode != 0:
        output = (result.stdout or result.stderr or "").strip()
        return {
            "allow": False,
            "message": (
                "Linter failed. Fix before committing.\n"
                f"{output[:2000]}\n"
                "How to fix: set CURSOR_LINT_CMD and run your lint fix command."
            ),
        }
    return {"allow": True}


def main() -> None:
    payload = json.loads(sys.stdin.read() or "{}")
    print(json.dumps(check(payload)))


if __name__ == "__main__":
    main()
