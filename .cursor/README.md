# `.cursor/` — Scaffold Vibe-Coding

> **Para que serve:** Template de governança Cursor para comparação com Claude Code.
> **Função:** Centralizar rules, hooks, commands, agents, skills, plans e MCP — sem credenciais reais no git.

Template de governança Cursor para comparação com Claude Code. Sem credenciais reais.

**Local (não commitar):** `.cursor/mcp.env` — copiar de `mcp.env.example`.

Guia completo: [docs/CURSOR_STRUCTURE_GUIDE.md](../docs/CURSOR_STRUCTURE_GUIDE.md)

---

## Catálogo de arquivos

| Arquivo / pasta | Para que serve | Função |
|-----------------|----------------|--------|
| **Raiz** | | |
| `README.md` | Este índice | Listar propósito de cada artefato em `.cursor/` |
| `MODEL_SELECTION_GUIDE.md` | Política de modelos | Escolher tier mínimo por complexidade da tarefa |
| `PARALLEL_AGENTS.md` | Paralelismo seguro | Definir quando subagents podem rodar em paralelo |
| `hooks.json` | Registro de hooks | Ligar eventos Cursor aos scripts em `hooks/` |
| `mcp.json` | Config MCP | Declarar servidores MCP (tokens via `mcp.env`) |
| `mcp.env.example` | Modelo de secrets MCP | Copiar → `mcp.env` local (gitignored) |
| `.cursorignore` | Exclusão de contexto | Evitar que o agente leia builds, secrets e lixo |
| **rules/** | Regras MDC | Injetar contexto always / glob / agent |
| `rules/core-rules/agent-behavior-always.mdc` | Comportamento base | Idioma, segurança, escopo e git (sempre ativo) |
| `rules/global-rules/token-economy-always.mdc` | Economia de tokens | Reduzir ruído de contexto em toda conversa |
| `rules/global-rules/knowledge-graph-agent.mdc` | Grafo de conhecimento | Orientar uso de grafo (template desativado) |
| `rules/tool-rules/git-workflow-agent.mdc` | Fluxo Git | Branches, commits e PRs sob demanda |
| `rules/tool-rules/docker-ops-agent.mdc` | Docker / infra | Compose e deploy local sob demanda |
| `rules/tool-rules/plan-architect-agent.mdc` | Planos multiagente | Formato obrigatório de `.plan.md` |
| `rules/example-stack-rules/api-patterns-auto.mdc` | Padrões API | Exemplo FastAPI ao editar `src/**/*.py` |
| `rules/example-stack-rules/audit-coverage-auto.mdc` | Auditoria | Cobertura e checklist ao tocar auditoria |
| `rules/testing-rules/test-patterns-auto.mdc` | Testes | Padrões pytest/httpx em `tests/**` |
| **hooks/** | Automação | Scripts Python acionados por `hooks.json` |
| `hooks/check-commit-msg.py` | Validação de commit | Exigir Conventional Commits em `git commit` |
| `hooks/check-linter.py` | Qualidade pré-commit | Bloquear commit se linter falhar (customizar) |
| `hooks/update-graph-on-session.py` | Sessão | Tarefa leve no início da sessão (grafo placeholder) |
| **commands/** | Slash commands | Fluxos repetíveis invocados no chat |
| `commands/review.md` | `/review` | Revisar diff não commitado (lint + segurança) |
| `commands/pr.md` | `/pr` | Preparar e abrir pull request |
| `commands/plano-otimizado.md` | `/plano-otimizado` | Gerar plano `.cursor/plans/*.plan.md` |
| `commands/multiagent.md` | `/multiagent` | Executar plano por fases com subagents |
| `commands/security-check.md` | `/security-check` | Auditoria rápida de segurança no diff |
| `commands/infra/infra-up.md` | `/infra-up` | Subir ambiente local de exemplo |
| **agents/** | Agentes especializados | Perfis com escopo e fluxo definidos |
| `agents/new-feature.md` | Nova feature | CRUD completo model → API → testes → frontend |
| `agents/security-audit.md` | Segurança | Varredura auth, inputs e credenciais |
| `agents/setup-environment.md` | Setup | Configurar env, deps e hooks no clone |
| **skills/** | Conhecimento sob demanda | Procedimentos longos fora das rules |
| `skills/create-feature/SKILL.md` | Skill create-feature | Fluxo discovery → plano → backend → testes |
| `skills/security-audit/SKILL.md` | Skill security-audit | Checklist de auditoria reutilizável |
| **plans/** | Planos gerados | Execução multiagente estruturada |
| `plans/example-feature_a1b2c3d4.plan.md` | Exemplo de plano | Modelo CRUD Item com fases F1..FN |
| `plans/archive/README.md` | Archive | Quando e por que arquivar planos concluídos |
| **notepads/** | Contexto `@Notepad` | Exemplos para copiar na UI do Cursor |
| `notepads/README.md` | Guia notepads | Quando usar notepad vs rule/skill |
| `notepads/Sprint_Context.example.md` | Sprint fictício | Objetivos e bloqueios da sprint |
| `notepads/API_Contract_v2.example.md` | Contrato API | Endpoints e schemas de exemplo |
