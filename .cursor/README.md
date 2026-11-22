# `.cursor/` — Scaffold Vibe-Coding

> **Para que serve:** Template de governança Cursor para comparação com Claude Code.
> **Função:** Centralizar rules, commands, agents, skills, plans e MCP — sem credenciais reais no git.

Template de governança Cursor para comparação com Claude Code. Sem credenciais reais.

**Local (não commitar):** `.cursor/mcp.env` — copiar de `mcp.env.example`.

Guia completo: [docs/CURSOR_STRUCTURE_GUIDE.md](../docs/CURSOR_STRUCTURE_GUIDE.md)

---

## Catálogo de arquivos

| Arquivo / pasta | Para que serve | Função |
|-----------------|----------------|--------|
| **Raiz** | | |
| `README.md` | Este índice | Listar propósito de cada artefato em `.cursor/` |
| `MODEL_SELECTION_GUIDE.md` | Política de modelos | Descoberta, catálogo, atribuição por custo/demanda e escalada |
| `models/catalog.yaml` | Catálogo local de modelos | Allow-list + ranks; só o orquestrador atualiza |
| `models/README.md` | Guia do catálogo | Quem escreve e onde ficam as atribuições por corrida |
| `PARALLEL_AGENTS.md` | Paralelismo seguro | Definir quando subagents podem rodar em paralelo |
| `mcp.json` | Config MCP | Declarar servidores MCP (tokens via `mcp.env`) |
| `mcp.env.example` | Modelo de secrets MCP | Copiar → `mcp.env` local (gitignored) |
| `.cursorignore` | Exclusão de contexto | Evitar que o agente leia builds, secrets e lixo |
| **rules/** | Regras MDC | Injetar contexto always / glob / agent |
| `rules/core-rules/agent-behavior-always.mdc` | Comportamento base | Idioma, segurança, escopo e git (sempre ativo) |
| `rules/core-rules/multiagent-loop-always.mdc` | Loop multiagente | Princípios: aceite, fail-closed, memória, autonomia |
| `rules/global-rules/token-economy-always.mdc` | Economia de tokens | Reduzir ruído de contexto em toda conversa |
| `rules/global-rules/knowledge-graph-agent.mdc` | Grafo de conhecimento | Orientar uso de grafo (template desativado) |
| `rules/tool-rules/git-workflow-agent.mdc` | Fluxo Git | Branches, commits e PRs sob demanda |
| `rules/tool-rules/docker-ops-agent.mdc` | Docker / infra | Compose e deploy local sob demanda |
| `rules/tool-rules/plan-architect-agent.mdc` | Planos multiagente | Formato obrigatório de `.plan.md` |
| `rules/example-stack-rules/api-patterns-auto.mdc` | Padrões API | Exemplo FastAPI ao editar `src/**/*.py` |
| `rules/example-stack-rules/ldap-auth-patterns-auto.mdc` | LDAP / Auth | TLS, escape RFC 4515, JWT cookie httpOnly, rate limiting |
| `rules/example-stack-rules/audit-coverage-auto.mdc` | Auditoria | Cobertura e checklist ao tocar auditoria |
| `rules/testing-rules/test-patterns-auto.mdc` | Testes | Padrões pytest/httpx em `tests/**` |
| **commands/** | Slash commands | Fluxos repetíveis invocados no chat |
| `commands/review.md` | `/review` | Revisor independente (critério + evidência) |
| `commands/pr.md` | `/pr` | Preparar e abrir pull request |
| `commands/plano-otimizado.md` | `/plano-otimizado` | Planejador: `.plan.md` com critério de aceite |
| `commands/multiagent.md` | `/multiagent` | Orquestrador: loop completo intake → entrega |
| `commands/security-check.md` | `/security-check` | Auditoria rápida de segurança no diff |
| `commands/infra/infra-up.md` | `/infra-up` | Subir ambiente local de exemplo |
| **agents/** | Agentes especializados | Perfis com escopo e fluxo definidos |
| `agents/intake.md` | Entrada | Fecha escopo e briefing com correlation ID |
| `agents/orchestrator.md` | Orquestrador | Risco, delegação, consolidação, memória durável |
| `agents/planner.md` | Planejador | Tarefas com aceite verificável |
| `agents/architect.md` | Arquiteto | Abordagem, ferramentas, rollback |
| `agents/engineer.md` | Engenheiro | Artefatos isolados + dry-run |
| `agents/executor.md` | Executor | Ações aprovadas + evidências |
| `agents/reviewer.md` | Revisor | Aprova/reprova sem raciocínio do executor |
| `agents/new-feature.md` | Nova feature | CRUD completo model → API → testes → frontend |
| `agents/security-audit.md` | Segurança | Varredura auth, inputs e credenciais |
| `agents/setup-environment.md` | Setup | Configurar env, deps e MCP no clone |
| **skills/** | Conhecimento sob demanda | Procedimentos longos fora das rules |
| `skills/multiagent-loop/SKILL.md` | Skill multiagent-loop | Loop engineering completo |
| `skills/create-feature/SKILL.md` | Skill create-feature | Fluxo discovery → plano → backend → testes |
| `skills/security-audit/SKILL.md` | Skill security-audit | Checklist de auditoria reutilizável |
| **memory/** | Memória em camadas | work / durable / log do loop |
| `memory/README.md` | Guia memória | Quem escreve em cada camada |
| **plans/** | Planos gerados | Execução multiagente estruturada |
| `plans/example-feature_a1b2c3d4.plan.md` | Exemplo de plano | Modelo CRUD Item com fases F1..FN |
| `plans/archive/README.md` | Archive | Quando e por que arquivar planos concluídos |
| **notepads/** | Contexto `@Notepad` | Exemplos para copiar na UI do Cursor |
| `notepads/README.md` | Guia notepads | Quando usar notepad vs rule/skill |
| `notepads/Sprint_Context.example.md` | Sprint fictício | Objetivos e bloqueios da sprint |
| `notepads/API_Contract_v2.example.md` | Contrato API | Endpoints e schemas de exemplo |
