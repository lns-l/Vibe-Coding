---
description: >
  Implementa feature de exemplo seguindo CLAUDE.md (model, service, router, tests, UI).
model: claude-sonnet-4-6
tools:
  - Read
  - Edit
  - Write
  - Bash
  - Grep
  - Glob
maxTurns: 40
---

> **Para que serve:** Subagent para implementar feature completa no Claude Code.
> **Função:** Seguir CLAUDE.md em model → service → router → testes → UI (template Acme).

# Agent: New Feature (template)

## Execution Flow

### PLAN
`.claude/plans/<slug>_<hash>.plan.md` se >3 arquivos.

### BACKEND
Model → service → router; só esta fase edita `src/main.py`.

### TESTS
401, 403, happy path, 422 — mocks para HTTP externo.

### FRONTEND
`api.ts` + tipos alinhados; sem `any`.

### VALIDATE
Lint + pytest/npm test verdes.

## Critério de conclusão

Comandos de validação do projeto retornam exit code 0.
