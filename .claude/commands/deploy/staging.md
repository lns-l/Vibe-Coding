---
description: "Deploy de exemplo para staging (template — confirmação obrigatória)"
allowed-tools:
  - Bash
  - Read
---

> **Para que serve:** Slash command `/deploy.staging` (fluxo fictício).
> **Função:** Checklist e passos de deploy para staging com confirmação explícita (template).

# /deploy.staging

Deploy fictício para ambiente `staging` (placeholder).

## Pré-requisitos

- Branch atual mergeável em `main`
- `/review` sem itens ❌ Crítico

## Fluxo

1. Confirmar com usuário: "Deploy staging agora? (s/N)"
2. Se não confirmado: parar
3. Executar pipeline placeholder: `echo "would deploy to staging"`

## Saída

Status do deploy ou motivo do cancelamento.

## Regras

- Nunca deploy sem confirmação explícita
- Nunca exibir secrets de CI no chat
