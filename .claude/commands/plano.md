---
description: "Generate plan in .claude/plans/<slug>_<hash8>.plan.md with acceptance criteria"
allowed-tools:
  - Bash
  - Read
  - Glob
  - Grep
  - Write
  - AskUserQuestion
---

> **Purpose:** Planner stage for the multi-agent engineering loop.
> **Função:** Discovery e plano com critério de aceite verificável por tarefa.

# /plano

Spec: `docs/MULTIAGENT_ENGINEERING_LOOP.md` §4.2

## Discovery (required)
- `git status`, `git diff --stat`, `git log -5`
- Scope and files per layer; critical files from `CLAUDE.md`
- Ask if ambiguous — fail closed

## Write
- Mermaid with real dependencies
- Behavioral changes (no implementation snippets)
- **Every phase:** objective, inputs, output format, acceptance criteria, risk, dependencies
- Max 8 phases
- Save `.claude/plans/<slug>_<hash8>.plan.md`
- Optional work copy: `.claude/memory/work/<correlation-id>/planner/`

## Exit gate
No handoff without verifiable acceptance on every task.
