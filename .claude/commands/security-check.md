---
description: "Auditoria rápida de segurança no diff atual"
allowed-tools:
  - Bash
  - Read
  - Grep
---

> **Para que serve:** Slash command `/security-check` no Claude Code.
> **Função:** Auditoria rápida de credenciais, inputs e rotas sensíveis no diff (template).

# /security-check

Analisa o diff por vulnerabilidades comuns.

## Verificações

1. Credenciais hardcoded ou arquivos sensíveis staged
2. Inputs externos sem validação de schema
3. Endpoints sem autenticação onde deveria haver
4. PII ou tokens em logs

## Saída

Relatório por categoria. Para checklist completo, usar agent `security-audit`.
