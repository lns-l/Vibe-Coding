---
description: "Revisa diff atual: lint, segurança e consistência (template)"
allowed-tools:
  - Bash
  - Read
  - Grep
---

> **Para que serve:** Slash command `/review` no Claude Code.
> **Função:** Revisar diff atual com lint, segurança e consistência antes do commit (template).

# /review

Revisa mudanças não commitadas antes do commit.

## Fluxo

1. Executar lint do projeto (`npm run lint` / `ruff check` — placeholders)
2. Verificar no diff: credenciais, auth ausente, `.env` staged
3. Verificar tipos e naming alinhados ao `CLAUDE.md`

## Saída

Sumário: ✅ OK / ⚠️ Atenção / ❌ Crítico — não corrigir sem aprovação.
