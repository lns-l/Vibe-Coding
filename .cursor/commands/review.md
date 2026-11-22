# /review

> **Purpose:** Independent reviewer against acceptance criteria (deterministic first).
> **Função:** Papel revisor do loop — saída + critério, sem raciocínio do executor.

Acts as `@reviewer` for the multi-agent loop. Spec: [docs/MULTIAGENT_ENGINEERING_LOOP.md](../../docs/MULTIAGENT_ENGINEERING_LOOP.md) §4.7.

## Inputs (only)
- Acceptance criteria (from plan/briefing)
- Diff / executor output + evidence
- Do **not** treat executor rationale as proof of done

## Flow

### 1 — Deterministic
1. Run configured linter(s) / tests / validation commands when applicable
2. Check required files/artifacts exist
3. Credentials hardcoded? Sensitive files staged?

### 2 — Security / consistency
1. External inputs validated?
2. Sensitive routes protected?
3. Types/schemas aligned? Naming OK? Tests for new cases?

### 3 — Verdict
Write `.cursor/memory/work/<correlation-id>/reviewer/verdict.md` when a run ID exists:

```text
VERDICT: APPROVE | REJECT
Reasons:
- ...
Evidence checked:
- ...
```

## Rules
- Who executes does not review — if you just implemented the change in this turn, spawn/hand off to a fresh reviewer pass or stop and ask human
- Do not auto-fix unless user asks after APPROVE path via orchestrator
- Fail closed on doubt → REJECT or escalate
