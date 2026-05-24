---
name: project-acme-catalog
description: Contexto atual do catálogo Acme (exemplo)
metadata:
  type: project
---

> **Para que serve:** Exemplo de memória `type: project` — contexto atual.
> **Função:** Manter branch, escopo e prioridades da feature em andamento (fictício).

Foco atual: endpoints de catálogo e webhooks de exemplo (branch `feature/webhooks-demo`).

**How to apply:** Novos routers seguem padrão em `src/routers/items.py`; registrar em `src/main.py` em série com outras fases.
