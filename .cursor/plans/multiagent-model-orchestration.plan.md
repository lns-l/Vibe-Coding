# Plan: Multi-agent model orchestration

> **Purpose:** Wire orchestrator-owned model discovery, local catalog, role assignment, and escalation.
> **Correlation:** `run-20261122-models`

## Objective
Enable `/multiagent` to discover platform-available models, persist them under `.cursor/models/`, assign the cheapest adequate model per role/task, and escalate + re-dispatch when a model fails the task.

## Acceptance criteria
- [x] Local catalog exists at `.cursor/models/catalog.yaml` with schema_version, models, role_defaults, escalation
- [x] `MODEL_SELECTION_GUIDE.md` documents discovery → assign → escalate → refresh
- [x] `/multiagent` documents triggers that authorize explicit per-role `model` on subagents
- [x] Orchestrator (Cursor + Claude) owns catalog updates and per-run assignments
- [x] Canonical loop docs (EN + PT-BR) include model orchestration section
- [x] Validate script checks catalog + guide presence
- [x] Reviewer default must differ from executor model family when possible

## Files affected
| File | Action |
|------|--------|
| `.cursor/models/catalog.yaml` | create |
| `.cursor/models/README.md` | create |
| `.cursor/MODEL_SELECTION_GUIDE.md` | rewrite |
| `.cursor/agents/orchestrator.md` | update |
| `.claude/agents/orchestrator.md` | update |
| `.cursor/commands/multiagent.md` | update |
| `.claude/commands/multiagent.md` | update |
| `.cursor/skills/multiagent-loop/SKILL.md` | update |
| `.cursor/rules/core-rules/multiagent-loop-always.mdc` | update |
| `docs/MULTIAGENT_ENGINEERING_LOOP.md` | update |
| `docs/MULTIAGENT_ENGINEERING_LOOP.pt-BR.md` | update |
| `docs/MULTIAGENT_LOOP_CHECKLIST.md` | update |
| `scripts/validate_multiagent_loop.py` | update |
| `.cursor/README.md` | update |

## Order
1. Catalog + README + guide
2. Orchestrator + commands + skill + always rule
3. Canonical docs EN/PT-BR + checklist
4. Validate script + README index
5. Run validate suite

## Dependencies
- Platform exposes available model slugs in-session (Cursor `available_subagent_models`) or via product UI/API
- Explicit user trigger (or `/multiagent`) authorizes passing `model` to subagents

## Risk
- Slugs drift as platform renames models → catalog refresh on each `/multiagent` mitigates
- Never store API keys in catalog; optional API probes use `config.env` only
