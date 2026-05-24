#!/usr/bin/env python3
"""Cursor hook: throttled task on sessionStart (knowledge graph placeholder)."""
# Purpose: optional background index/graph update; no-op unless configured.

from __future__ import annotations

import json
import os
import subprocess
import sys
import threading
import time

INTERVAL_SECONDS = int(os.getenv("GRAPH_SESSION_INTERVAL", "14400"))
TS_FILE = os.path.join(".cursor", ".graph_session_ts")
UPDATE_CMD = os.getenv("GRAPH_UPDATE_CMD", "").split()


def should_update() -> bool:
    if os.getenv("GRAPH_SESSION_HOOK", "off") != "on":
        return False
    if not os.path.exists(TS_FILE):
        return True
    try:
        last = float(open(TS_FILE, encoding="utf-8").read().strip())
    except (OSError, ValueError):
        return True
    return (time.time() - last) > INTERVAL_SECONDS


def update() -> None:
    if not should_update():
        return
    if UPDATE_CMD:
        subprocess.Popen(
            UPDATE_CMD,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    os.makedirs(os.path.dirname(TS_FILE), exist_ok=True)
    with open(TS_FILE, "w", encoding="utf-8") as handle:
        handle.write(str(time.time()))


def main() -> None:
    # Cursor may pass JSON on stdin; we only need to acknowledge success
    _ = sys.stdin.read()
    threading.Thread(target=update, daemon=True).start()
    print(json.dumps({"allow": True}))


if __name__ == "__main__":
    main()
