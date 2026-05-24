# @Sprint_Context (exemplo fictício)

> **Para que serve:** Modelo de contexto de sprint para copiar em um Notepad.
> **Função:** Manter objetivos, decisões, bloqueios e referências da sprint atual visíveis ao agente.

**Sprint:** 2026-W21 — Acme API  
**Objetivo:** Entregar CRUD Widget + hardening de auth

## Decisões tomadas
- JWT com TTL 15min; refresh em cookie httpOnly
- Widget.sku único por tenant (não global)
- Frontend: manter padrão de `ItemsPage.tsx`

## Fora de escopo
- Webhooks (sprint seguinte)
- Migração de dados legados

## Bloqueios
- Nenhum (ambiente local OK)

## Referências
- Plano: `.cursor/plans/widget-crud_a1b2c3d4.plan.md`
- Issue fictícia: ACME-142
