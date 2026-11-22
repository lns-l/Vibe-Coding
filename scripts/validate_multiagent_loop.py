#!/usr/bin/env python3
"""Validate multi-agent engineering loop scaffold artifacts.

Exit 0 when required docs, agents, commands, memory layers, and example plan
acceptance markers are present. No network; no secrets.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "docs/MULTIAGENT_ENGINEERING_LOOP.md",
    "docs/MULTIAGENT_ENGINEERING_LOOP.pt-BR.md",
    "docs/MULTIAGENT_LOOP_CHECKLIST.md",
    ".cursor/rules/core-rules/multiagent-loop-always.mdc",
    ".cursor/skills/multiagent-loop/SKILL.md",
    ".cursor/commands/multiagent.md",
    ".cursor/commands/plano-otimizado.md",
    ".cursor/commands/review.md",
    ".cursor/PARALLEL_AGENTS.md",
    ".cursor/MODEL_SELECTION_GUIDE.md",
    ".cursor/models/catalog.yaml",
    ".cursor/models/README.md",
    ".cursor/memory/README.md",
    ".claude/commands/multiagent.md",
    ".claude/commands/plano.md",
    ".claude/commands/review.md",
    ".claude/memory/README.md",
]

ROLES = [
    "intake",
    "orchestrator",
    "planner",
    "architect",
    "engineer",
    "executor",
    "reviewer",
]

MEMORY_DIRS = [
    ".cursor/memory/work",
    ".cursor/memory/durable",
    ".cursor/memory/log",
    ".claude/memory/work",
    ".claude/memory/durable",
    ".claude/memory/log",
]

EXAMPLE_PLAN = ROOT / ".cursor/plans/example-feature_a1b2c3d4.plan.md"
MODEL_CATALOG = ROOT / ".cursor/models/catalog.yaml"
CATALOG_REQUIRED_MARKERS = (
    "schema_version:",
    "models:",
    "role_defaults:",
    "escalation:",
)


def main() -> int:
    failures: list[str] = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.is_file():
            failures.append(f"missing file: {rel}")

    for role in ROLES:
        for base in (".cursor/agents", ".claude/agents"):
            rel = f"{base}/{role}.md"
            if not (ROOT / rel).is_file():
                failures.append(f"missing agent: {rel}")

    for rel in MEMORY_DIRS:
        if not (ROOT / rel).is_dir():
            failures.append(f"missing dir: {rel}")

    if EXAMPLE_PLAN.is_file():
        text = EXAMPLE_PLAN.read_text(encoding="utf-8")
        if "Acceptance criteria" not in text and "acceptance criteria" not in text.lower():
            failures.append("example plan missing acceptance criteria")
    else:
        failures.append(f"missing file: {EXAMPLE_PLAN.relative_to(ROOT).as_posix()}")

    if MODEL_CATALOG.is_file():
        catalog_text = MODEL_CATALOG.read_text(encoding="utf-8")
        for marker in CATALOG_REQUIRED_MARKERS:
            if marker not in catalog_text:
                failures.append(f"model catalog missing marker: {marker}")
    else:
        failures.append("missing file: .cursor/models/catalog.yaml")

    if failures:
        print("FAIL — multi-agent loop scaffold")
        for item in failures:
            print(f"  - {item}")
        return 1

    print("PASS — multi-agent loop scaffold")
    print(
        f"  checked {len(REQUIRED_FILES)} files, {len(ROLES)} roles x2, "
        f"{len(MEMORY_DIRS)} memory dirs, model catalog"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
