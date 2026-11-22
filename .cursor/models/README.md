# `.cursor/models/` — Platform model catalog

> **Purpose:** Local, orchestrator-owned inventory of models available on the current platform.
> **Função:** Catálogo local de modelos liberados; só o orquestrador atualiza.

## Files

| File | Role |
|------|------|
| `catalog.yaml` | Source of truth for available slugs, cost/capability ranks, role defaults, escalation |
| `README.md` | This guide |

## Who writes

- **Orchestrator only** refreshes `catalog.yaml` when `/multiagent` runs (or on explicit model-refresh request).
- Other roles **read** the catalog / per-run assignment; they never edit it.

## Per-run assignments

Written under:

`.cursor/memory/work/<correlation-id>/orchestrator/model_assignments.md`

## Secrets

Never store API keys, tokens, or account credentials here. Optional API probes use `config.env` / secrets manager only.
