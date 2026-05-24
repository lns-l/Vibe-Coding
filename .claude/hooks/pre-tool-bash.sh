#!/usr/bin/env bash
# Claude hook (PreToolUse/Bash): block dangerous shell patterns (template).
# Purpose: reject rm -rf /, dd, chmod 777, etc. before bash runs.

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

DANGEROUS_PATTERNS=(
  'rm -rf /'
  'dd if='
  '> /dev/sd'
  'chmod 777'
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    jq -n \
      --arg reason "Command blocked by policy: matched pattern $pattern" \
      '{hookSpecificOutput: {permissionDecision: "deny", permissionDecisionReason: $reason}}'
    exit 0
  fi
done

echo '{"continue": true}'
exit 0
