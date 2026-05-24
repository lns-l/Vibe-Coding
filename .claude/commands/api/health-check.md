---
description: "Verifica endpoints de saúde da API fictícia Acme"
allowed-tools:
  - Bash
  - Read
---

> **Para que serve:** Slash command `/api.health-check` para API fictícia Acme.
> **Função:** Localizar e validar rota `/health` e resposta esperada (template).

# /api.health-check

Valida configuração de health da API (template).

1. Ler `src/main.py` (ou equivalente) e localizar rota `/health`
2. Se servidor local estiver rodando: `curl -sf http://localhost:8000/health` (ajuste porta)
3. Reportar: status HTTP, corpo da resposta, tempo de resposta

Se `$ARGUMENTS` informar URL base, usar essa base em vez de localhost.
