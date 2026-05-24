---
description: "Gera plano em .claude/plans/<slug>_<hash8>.plan.md"
allowed-tools:
  - Bash
  - Read
  - Glob
  - Grep
---

> **Para que serve:** Slash command `/plano` no Claude Code.
> **Função:** Discovery obrigatório e geração de `.claude/plans/<slug>_<hash>.plan.md` (template).

# /plano

Gera plano multiagente após discovery completo.

## Discovery (obrigatório)

- `git status`, `git diff --stat`, `git log -5`
- Escopo e arquivos por camada
- Arquivos críticos do `CLAUDE.md`
- Perguntar se ambíguo

## Escrita

- Mermaid com dependências reais
- Mudanças comportamentais (sem snippets)
- Máximo 8 fases
- Salvar em `.claude/plans/<slug>_<hash8>.plan.md`
