# /plano-otimizado

> **Purpose:** Planner-stage slash command — produce a `.plan.md` with acceptance criteria.
> **Função:** Discovery e plano multiagente alinhado ao loop engineering.

Generates `.cursor/plans/<slug>_<hash8>.plan.md` as the **planner** output for `/multiagent`.

## Phase 1 — Discovery (required)
1. `git status`, `git diff --stat`, `git log --oneline -5`
2. User scope and business objective (or load intake briefing)
3. Map reference files; read `PARALLEL_AGENTS.md` for critical paths
4. If ambiguous: stop and ask (fail closed) — do not invent scope

## Phase 2 — Partitioning
- One phase = cohesive deliverable
- Each phase **must** include verifiable acceptance criteria
- Mark risk: read / reversible / irreversible
- Flag `requires_human_approval` when external effect
- Independent → parallel only if file sets disjoint; 2–8 phases

## Phase 3 — Models
- Assign minimum sufficient tier (`MODEL_SELECTION_GUIDE.md`)

## Phase 4 — Write
- Follow `plan-architect-agent.mdc`
- Hash8 = first 8 chars of `git rev-parse HEAD`
- Write work copy under `.cursor/memory/work/<correlation-id>/planner/` when a run ID exists

## Exit gate
Every task/phase has verifiable acceptance criteria. Otherwise do not hand off to architect/executor.

## Output
Summary: phases, parallel batches, risk class, human gates, suggested parent model
