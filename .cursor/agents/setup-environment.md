---
name: setup-environment
description: >
  Orienta setup local do projeto fictício Acme API: deps, env, MCP, hooks.
  Use quando pedir "configurar ambiente" ou "primeiro clone".
readonly: false
---

> **Para que serve:** Agente de onboarding do ambiente local do template.
> **Função:** Orientar cópia de `.env`, deps, MCP, hooks e validação após primeiro clone.

# Agent: Setup Environment

## Pré-requisitos (template)
- Python 3.12+ ou Node 20+ (conforme stack do projeto)
- Docker Desktop (opcional, para MCP GitHub)
- Git e gh CLI

## Fluxo

### [1 — ENV]
1. Copiar `.env.example` → `.env` (valores fictícios apenas)
2. Copiar `.cursor/mcp.env.example` → `.cursor/mcp.env` (token placeholder)

### [2 — DEPS]
1. Instalar dependências (`pip install -r requirements.txt` ou `npm install`)
2. Validar com comando de smoke test do projeto

### [3 — CURSOR]
1. Confirmar rules em `.cursor/rules/` indexadas
2. Hooks: testar `python .cursor/hooks/check-commit-msg.py`
3. MCP: reiniciar Cursor após `mcp.env`; validar indicador verde

### [4 — HOOKS OPCIONAIS]
- `CURSOR_LINT_HOOK=on` + `CURSOR_LINT_CMD="ruff check src"`
- `GRAPH_SESSION_HOOK=on` + `GRAPH_UPDATE_CMD="echo graph-placeholder"`

## Constraints
- Nunca commitar `.env` ou `mcp.env`
- Nunca usar tokens reais em exemplos versionados

## Saída
Checklist ✅/❌ por etapa + próximos passos
