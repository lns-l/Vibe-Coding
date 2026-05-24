#!/usr/bin/env bash
# Claude hook (PostToolUse Edit|Write): optional lint after edits (template).
# Purpose: run project linter when CLAUDE_LINT_HOOK=on; otherwise no-op.

set -euo pipefail

if [ "${CLAUDE_LINT_HOOK:-off}" != "on" ]; then
  exit 0
fi

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // ""')

if [[ "$FILE" =~ \.(ts|tsx|js|jsx)$ ]]; then
  if command -v npx >/dev/null 2>&1; then
    npx eslint "$FILE" --quiet 2>&1 || {
      echo "Lint failed on $FILE. Run: npm run lint" >&2
      exit 2
    }
  fi
fi

exit 0
