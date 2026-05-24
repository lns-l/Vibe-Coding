---
description: "Executa .plan.md em batches com subagents e worktrees"
allowed-tools:
  - Bash
  - Read
  - Agent
  - TodoWrite
---

> **Para que serve:** Slash command `/multiagent` no Claude Code.
> **Função:** Executar plano `.plan.md` em batches com subagents e worktrees (template).

# /multiagent

Argumento: caminho do plano, ex. `.claude/plans/example-feature_a1b2c3d4.plan.md`

## Fases

1. Parse frontmatter + Mermaid → batches
2. Validar disjunção de arquivos; respeitar críticos do `CLAUDE.md`
3. Executar batches com `isolation: "worktree"` quando paralelo
4. Consolidar; integrar arquivos críticos no parent
5. Encerramento: validação + `todo.status` completed

## Regras

- Nunca paralelizar fases com arquivo em comum
- TodoWrite: uma fase `in_progress` por vez no parent
