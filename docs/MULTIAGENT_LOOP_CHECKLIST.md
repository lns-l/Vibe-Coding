# Multi-agent loop — go-live checklist & initial suite

> **Purpose:** Operational checklist (§10) plus a minimal validation suite for the loop scaffold.
> **Função:** Checklist de uso e suíte inicial que valida a presença dos artefatos do fluxo.

Canonical: [MULTIAGENT_ENGINEERING_LOOP.md](MULTIAGENT_ENGINEERING_LOOP.md).

## Go-live checklist

- [ ] Each role has scope, tools, and limits (see `.cursor/agents/` and `.claude/agents/`)
- [ ] Every task has verifiable acceptance criteria (`plan-architect-agent.mdc`)
- [ ] Iteration / cost / time limits configured (defaults in `multiagent-loop-always.mdc`)
- [ ] Human approval active for irreversible actions (orchestrator + architect flags)
- [ ] Reviewer independent from executor (`@reviewer`, `/review`)
- [ ] Durable memory writable only by orchestrator (`.cursor/memory/durable/`, `.claude/memory/durable/`)
- [ ] Model catalog present (`.cursor/models/catalog.yaml`); orchestrator-only refresh; guide in `MODEL_SELECTION_GUIDE.md`
- [ ] Append-only log with correlation ID (`.cursor/memory/log/`)
- [ ] Initial suite runs (below)
- [ ] Shadow-mode pilot completed with metrics (team process — not automated here)

## Initial suite (scaffold)

Run from repo root:

```bash
python scripts/validate_multiagent_loop.py
# Windows alternative if `python` is missing:
# powershell -File scripts/validate_multiagent_loop.ps1
```

Expected: exit code `0` and a pass list for required paths/agents/commands.

### What the suite checks
1. Canonical docs exist (EN + PT-BR)
2. Always-on rule `multiagent-loop-always.mdc` exists
3. All seven role agents exist in Cursor and Claude
4. `/multiagent`, planner, and `/review` commands exist in both scaffolds
5. Memory layers `work/`, `durable/`, `log/` exist
6. Skill `multiagent-loop/SKILL.md` exists
7. Example plan contains the string `Acceptance criteria`
8. Model catalog `.cursor/models/catalog.yaml` and `MODEL_SELECTION_GUIDE.md` exist

### Manual smoke (shadow mode)
1. `/multiagent` on a read-only ask → briefing + risk `read` → delivery without durable promote of secrets
2. Plan with missing acceptance → must stop at planner gate
3. Simulated irreversible step → must request human approval before executor
