#!/usr/bin/env bash
# Claude hook (SessionStart): throttled placeholder for graph/index update.
# Purpose: rate-limit heavy startup tasks via GRAPH_SESSION_INTERVAL (default 4h).

set -euo pipefail

TS_FILE=".claude/.session_hook_ts"
INTERVAL="${GRAPH_SESSION_INTERVAL:-14400}"

if [ "${GRAPH_SESSION_HOOK:-off}" != "on" ]; then
  exit 0
fi

NOW=$(date +%s)
if [ -f "$TS_FILE" ]; then
  LAST=$(cat "$TS_FILE")
  DIFF=$((NOW - LAST))
  if [ "$DIFF" -lt "$INTERVAL" ]; then
    exit 0
  fi
fi

# Placeholder: run background index/graph update when GRAPH_UPDATE_CMD is set
if [ -n "${GRAPH_UPDATE_CMD:-}" ]; then
  eval "$GRAPH_UPDATE_CMD" >/dev/null 2>&1 &
fi

echo "$NOW" > "$TS_FILE"
exit 0
