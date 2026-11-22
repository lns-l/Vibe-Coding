# Model selection guide

> **Purpose:** How the orchestrator discovers, catalogs, assigns, and escalates models in this repo.
> **Função:** Descoberta → catálogo local → atribuição por custo/demanda → escalada e re-disparo.

Canonical loop: [docs/MULTIAGENT_ENGINEERING_LOOP.md](../docs/MULTIAGENT_ENGINEERING_LOOP.md)  
Local catalog: [models/catalog.yaml](models/catalog.yaml)

## Principle

Use the **cheapest available model that meets the demand**. Escalate only with evidence of failure. Never invent slugs that are not in the live platform allow-list.

## Trigger (authorizes per-role `model`)

Model orchestration is **on** when any of these is true:

| Trigger | Meaning |
|---------|---------|
| `/multiagent` | Full loop — orchestrator refreshes catalog and assigns models |
| `/multiagent --models` | Same, force catalog refresh before assign |
| `/multiagent --refresh-models` | Refresh catalog only (optional), report diff |
| User text | Explicit phrases: "usar seleção de modelos", "multi-model", "defaults por papel", "orquestrar modelos" |

Without a trigger, subagents inherit the parent chat model (platform default).  
With a trigger, passing an explicit `model` slug to each role subagent is **user-authorized**.

## Flow

```text
Trigger
  → Orchestrator discovers platform-available models
  → Updates .cursor/models/catalog.yaml (available flags + last_refresh)
  → Scores demand (risk, role, task complexity)
  → Picks lowest cost_rank among eligible available models
  → Writes work/<id>/orchestrator/model_assignments.md
  → Dispatches role with explicit model slug
  → On MODEL_INSUFFICIENT / quality fail → escalate model → re-dispatch
  → After max escalations → human
```

## 1. Discovery (orchestrator)

Sources (in order):

1. **Cursor session** — slugs in `available_subagent_models` (live agent context)
2. **Claude Code UI** — models selectable for Agent/Task in this project
3. **Optional provider APIs** — list-models only if configured via `config.env` / `*_FILE` (never hardcode keys; never write secrets into the catalog)

Rules:

- Mark catalog entries `available: true` only if present in the live allow-list
- Add new live slugs with provisional `cost_rank` / `capability_rank`; prefer documenting uncertainty in `notes`
- Remove or set `available: false` for slugs no longer offered
- Update `last_refresh.at`, `last_refresh.source`, `updated_by: orchestrator`
- Refresh when: `/multiagent` starts, `--refresh-models`, allow-list mismatch, or catalog older than the session policy

## 2. Assignment

For each role/task:

1. Load `role_defaults` from `catalog.yaml`
2. Apply `demand_overrides` (security, mechanical, cross-module, etc.)
3. Filter: `available == true` AND meets `min_capability_rank` AND within `max_cost_rank` when possible
4. Prefer models whose `strengths` intersect `prefer_strengths`
5. Choose **lowest `cost_rank`**; tie-break: higher `capability_rank`, then stable slug order
6. **Reviewer:** if `must_differ_from_role: executor`, pick a different `family` when another eligible model exists
7. Record choice + rationale in `model_assignments.md`

If no model fits `max_cost_rank`, widen cost by one step rather than picking an unavailable slug.

## 3. Escalation and re-dispatch

When a role returns to the orchestrator with:

| Code | Meaning |
|------|---------|
| `MODEL_INSUFFICIENT` | Model cannot complete the task (quality/context/tools) |
| `ACCEPTANCE_FAIL_QUALITY` | Reviewer/deterministic checks fail in a way that suggests under-powered model |
| `TOOL_OR_CONTEXT_LIMIT` | Context or tool ceiling hit |

Orchestrator:

1. Selects the next model with **higher `capability_rank`**, allowing higher `cost_rank`
2. Does not reuse the failed slug for that task in this run
3. Appends escalation to `model_assignments.md` and the run log
4. **Re-dispatches the same task** with the new model (same acceptance criteria)
5. Stops after `escalation.max_model_escalations_per_task` (default 3) → escalate human

Model escalation is **independent** of the review rejection budget (max 3 rejects / 2 no-progress rounds), but both can trigger human escalation.

## 4. Agent contract on failure

Role agents must **not** silently continue with a bad fit. Return to orchestrator:

```markdown
## Model failure
- code: MODEL_INSUFFICIENT
- slug: <used-slug>
- task_id: <id>
- evidence: <what failed>
- suggestion: <optional capability need>
```

## 5. Thinking

- Use higher-capability / thinking-oriented models only for non-obvious decisions (2+ options), critical-module impact, or security
- Cap thinking-heavy phases (~2 per plan); keep mechanical phases on economy tiers

## 6. Anti-patterns

- ❌ Hardcoding a forever slug in an agent file without catalog refresh
- ❌ Picking a slug not in the live platform allow-list
- ❌ Storing API keys in `catalog.yaml`
- ❌ Executor and reviewer forced to the same family when alternatives exist
- ❌ Escalating cost without a failure code / evidence
