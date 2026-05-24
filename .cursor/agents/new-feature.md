---
name: new-feature
description: >
  Implementa feature completa (model → API → testes → frontend).
  Use para CRUD ou fluxo novo de entidade fictícia.
readonly: false
---

> **Para que serve:** Agente especializado em implementar feature completa (CRUD fictício).
> **Função:** Orquestrar plano, backend, testes, frontend e validação seguindo o skill `create-feature`.

# Agent: Nova Feature

## Execution Flow

### [PLAN]
Criar `.cursor/plans/<entidade>_<hash>.plan.md` se escopo ≥ 5 arquivos.

### [MODELO / SCHEMA]
- Entidade tipada; schemas request/response
- Sem campos sensíveis no response

### [LÓGICA]
- Service com validação de entrada
- Auditoria em mutações (se aplicável)

### [API]
- Auth + autorização; `response_model` explícito
- Registrar rota no ponto central

### [TESTES]
- 401, 403, 200/201, 422

### [FRONTEND]
- Tipos alinhados; HTTP via client central

### [VALIDATE]
- Lint + testes verdes

## Final Checklist
- [ ] Sem credenciais hardcoded
- [ ] Inputs validados
- [ ] Endpoints protegidos
- [ ] Conventional Commits

## Skills
- `@create-feature` para fluxo detalhado
