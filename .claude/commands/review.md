---
description: "Independent reviewer: acceptance criteria + evidence; deterministic first"
allowed-tools:
  - Bash
  - Read
  - Grep
  - Write
---

> **Purpose:** Independent review stage of the multi-agent engineering loop.
> **Função:** Revisor — saída + critério; checagens determinísticas primeiro.

# /review

Spec: `docs/MULTIAGENT_ENGINEERING_LOOP.md` §4.7

## Inputs only
- Acceptance criteria
- Diff / executor output + evidence
- Do not treat executor rationale as proof

## Flow
1. Deterministic: lint/tests/validation commands; required artifacts present
2. Security: credentials, auth gaps, staged secrets
3. Consistency vs `CLAUDE.md`
4. Verdict: **APPROVE** or **REJECT** with reasons
5. Optional write: `.claude/memory/work/<correlation-id>/reviewer/verdict.md`

## Rules
- Who executes does not review
- Do not auto-fix without approval
- Fail closed → REJECT or escalate
