---
description: "Run the multi-agent engineering loop (intake → delivery) with model orchestration"
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Agent
  - TodoWrite
  - AskUserQuestion
---

> **Purpose:** Orchestrator entry for the multi-agent engineering loop.
> **Função:** Executar o fluxo completo com subagents, memória em camadas e seleção de modelos.

# /multiagent

Spec: `docs/MULTIAGENT_ENGINEERING_LOOP.md`  
Models: `.cursor/MODEL_SELECTION_GUIDE.md` · `.cursor/models/catalog.yaml`

## Arguments
- `/multiagent` — full loop; **model orchestration on**
- `/multiagent --models` — force catalog refresh, then run
- `/multiagent --refresh-models` — refresh catalog from live allow-list; report
- Optional plan path or correlation ID

Natural-language triggers: "usar seleção de modelos", "multi-model", "defaults por papel", "orquestrar modelos".

## Stages
0. Orchestrator: discover platform models → refresh catalog → assign cheapest adequate per role → `model_assignments.md`
1. Intake → briefing + correlation ID
2. Orchestrator risk class
3. Planner → acceptance criteria per task
4. Architect → tools, risks, rollback
5. Engineer → isolated work + dry-run
6. Human approval if external effect
7. Executor → evidence (explicit model from assignment)
8. Reviewer → APPROVE/REJECT (independent; prefer different family than executor)
9. Orchestrator consolidate + durable promote + log
10. Retro → tests from defects

## Model escalation
On `MODEL_INSUFFICIENT` / quality model-fail: orchestrator picks a higher-capability model and **re-dispatches** the same task. Exhausted escalations → human.

## Rules
- Who executes does not review
- Only orchestrator updates `.cursor/models/catalog.yaml` and durable memory
- Disjoint files only when parallel; respect critical files in `CLAUDE.md`
- Max 3 review rejections or 2 no-progress rounds → escalate
- Never claim success without evidence
- Never invent slugs outside the live allow-list; never store secrets in the catalog
