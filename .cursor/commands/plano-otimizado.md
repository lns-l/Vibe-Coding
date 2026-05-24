# /plano-otimizado

> **Para que serve:** Slash command de planejamento multiagente no Cursor.
> **Função:** Discovery obrigatório e geração de `.cursor/plans/<slug>_<hash>.plan.md` (template).

Gera plano multiagente em `.cursor/plans/<slug>_<hash8>.plan.md` (template).

## Fase 1 — Discovery (obrigatório)
1. `git status`, `git diff --stat`, `git log --oneline -5`
2. Escopo do usuário e objetivo de negócio
3. Mapear model, service, router, testes, frontend de referência
4. Ler `PARALLEL_AGENTS.md` — marcar arquivos críticos
5. Se ambíguo: parar e perguntar

## Fase 2 — Particionamento
- Uma fase = unidade entregável coesa
- Ordem: Models → Services → Routers → Tests → Frontend → Encerramento
- 2–8 fases; paralelo só com arquivos disjuntos

## Fase 3 — Modelos
- Atribuir tier por fase (ver `MODEL_SELECTION_GUIDE.md`)

## Fase 4 — Escrita
- Seguir `plan-architect-agent.mdc`
- Hash8 = primeiros 8 chars de `git rev-parse HEAD`

## Saída
Resumo: fases, batches paralelos, modelo parent sugerido
