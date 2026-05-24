# /multiagent

> **Para que serve:** Slash command que executa um plano `.plan.md` gerado por `/plano-otimizado`.
> **Função:** Parsear fases, rodar batches paralelos com arquivos disjuntos e consolidar resultado (template).

Executa plano `.plan.md` em batches paralelos seguros (template).

## Argumento
`/multiagent @caminho/do/plano.plan.md`

## Fase 1 — Parse
1. Ler frontmatter e todos os F-IDs
2. Construir grafo a partir do Mermaid
3. Montar batches (fases sem dependências pendentes)
4. **Validar disjunção de arquivos** entre fases do mesmo batch
5. Fases com arquivo crítico → nunca em paralelo

## Fase 2 — Execução
- Cada Task recebe: Contexto, Convenções, seção da fase F-N
- Ao terminar: `.cursor/plans/agent-FN-done.md`
- Aguardar batch completo antes do próximo

## Fase 3 — Consolidação
- Imports compatíveis entre fases paralelas?
- Integração em arquivos críticos: manual, não delegada

## Fase 4 — Encerramento
1. Comando de validação do plano
2. Lint se necessário
3. Remover `agent-FN-done.md` temporários

## Regras absolutas
- Nunca paralelizar fases com arquivo em comum
- Nunca declarar sucesso antes da validação passar
