---
description: "Commit, push e abre PR com descrição do diff"
allowed-tools:
  - Bash
  - Read
---

> **Para que serve:** Slash command `/pr` no Claude Code.
> **Função:** Commit, push e abertura de PR com descrição do diff (template).

# /pr

1. `git diff` — entender mudanças
2. Se lint falhou: avisar e sugerir `/review`
3. Commit com Conventional Commits
4. `git push -u origin HEAD`
5. `gh pr create` — título < 70 chars + test plan

## Regras

- Nunca commitar `.env`, `mcp.env` ou secrets
- Nunca force push sem confirmação explícita
