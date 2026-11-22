# Safe parallelism protocol (multi-agent loop)

> **Purpose:** Rules for parallel subagents without file conflicts or review contamination.
> **Função:** Disjunção de arquivos, espaços isolados por papel e checklist pré-paralelo.

Canonical loop: [docs/MULTIAGENT_ENGINEERING_LOOP.md](../docs/MULTIAGENT_ENGINEERING_LOOP.md).

## Fundamental rule
Parallelize **only** when file sets are **disjoint**.

## Role isolation
- Each role writes only under `.cursor/memory/work/<correlation-id>/<role>/`
- No concurrent writers on the same path
- Reviewer must not receive executor reasoning — only output + acceptance criteria

## Critical files — never in parallel
Replace with real project paths:

| File | Reason |
|------|--------|
| `backend/app/main.py` | Router/middleware registration |
| `backend/app/config.py` | Central settings |
| `frontend/src/services/core/api.ts` | HTTP client base |
| `docker-compose.yml` | Local orchestration |

## Safe combinations
- ✅ Backend routers ↔ Frontend pages (no shared critical entry)
- ✅ New tests ↔ source (tests do not edit source)
- ⚠️ Two backend modules — check shared imports
- ❌ Any phase ↔ critical entry/config in parallel

## Pre-parallel checklist
- [ ] Phase file sets disjoint?
- [ ] No critical file shared in the batch?
- [ ] Each agent has enough context (criteria, not peer chain-of-thought)?
- [ ] Merge/integration order after parallel clear?
- [ ] Each phase has verifiable acceptance criteria?

## Conflict example

```
F1: src/models/user.ts, src/schemas/user.ts
F2: src/pages/UserPage.tsx
→ Empty intersection ✅

F3: src/routes/users.ts, src/app.ts
F4: src/routes/groups.ts, src/app.ts
→ Intersection: src/app.ts ❌ serialize F3 and F4
```
