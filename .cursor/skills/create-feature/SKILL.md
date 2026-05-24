# Skill: Create Feature

> **Para que serve:** Procedimento sob demanda para criar entidade/CRUD nova.
> **Função:** Guiar discovery, plano, backend, testes e frontend com padrões do template Acme API.

## Quando esta skill é relevante
- CRUD ou fluxo novo para uma entidade
- Usuário pede "nova feature" ou "adicionar entidade X"

## Fluxo resumido

1. **Discovery** — mapear model, service, router, testes e frontend de referência
2. **Plano** — `.cursor/plans/<entidade>_<hash>.plan.md` se 5+ arquivos
3. **Backend** — schema → service → router (auth + validação)
4. **Testes** — 401, 403, sucesso, 422
5. **Frontend** — tipos alinhados, sem `any` injustificado
6. **Validação** — lint + testes verdes

## Referências no projeto
- Invocar agent `@new-feature` para fluxo completo
- Rule `api-patterns-auto.mdc` para endpoints
- Rule `test-patterns-auto.mdc` para testes

## Anti-padrões
- ❌ Credenciais hardcoded
- ❌ Endpoint sem autenticação quando sensível
- ❌ Commit sem Conventional Commits
