---
name: feedback-testing-approach
description: Preferência de testes — sem mock de banco em integração
metadata:
  type: feedback
---

> **Para que serve:** Exemplo de memória `type: feedback` sobre testes.
> **Função:** Registrar preferência do time para o modelo não repetir anti-padrões (fictício).

Não mockar banco em testes de integração do domínio de itens.

**Why:** Divergência de schema entre mock e DB real causou regressão em projeto anterior (fictício).

**How to apply:** Usar fixtures em DB de teste; mock apenas APIs HTTP externas.
