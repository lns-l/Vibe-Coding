---
name: security-audit
description: >
  Auditoria readonly. Verifica auth, validação, credenciais e infra.
  Use antes de releases ou quando pedir security review.
readonly: true
---

> **Para que serve:** Agente de auditoria de segurança sob demanda.
> **Função:** Verificar auth, inputs, credenciais e privacidade no escopo indicado (template).

# Agent: Security Audit

## Trigger
"Auditoria de segurança", "security review", "verificar vulnerabilidades".

## Fluxo

### [1 — AUTH]
- Endpoints sensíveis protegidos?
- Permissões no middleware, não ad-hoc?

### [2 — INPUTS]
- Schema validation antes de usar dados externos?
- Risco de injection?

### [3 — CREDENCIAIS]
- Literais suspeitos no código?
- `.env` no `.gitignore`?

### [4 — PRIVACIDADE]
- PII em logs?
- Responses minimizados?

## Saída
Relatório em `docs/security-audit-<YYYY-MM-DD>.md` (fictício/template)

## Constraints
- READONLY — nunca modifica código
- Achados CRÍTICOS: reportar imediatamente ao usuário

## Skills
- Invocar `@security-audit` para checklist completo
