# `.claude/` — Scaffold Vibe-Coding

> **Para que serve:** Template de governança Claude Code para comparação com Cursor.
> **Função:** Centralizar settings, commands, subagents, plans e exemplos de memória — sem secrets no git.

Template de governança Claude Code para comparação com Cursor. Sem credenciais reais.

**Local (não commitar):** `CLAUDE.local.md`, `.claude/settings.local.json` — ver `.example` na raiz e aqui.

Guia completo: [docs/CLAUDE_CODE_GUIDE.md](../docs/CLAUDE_CODE_GUIDE.md)

---

## Catálogo de arquivos

| Arquivo / pasta | Para que serve | Função |
|-----------------|----------------|--------|
| **Raiz** | | |
| `README.md` | Este índice | Listar propósito de cada artefato em `.claude/` |
| `settings.json` | Config versionada | Permissões, MCP, modelo e env de exemplo |
| `settings.local.json.example` | Overrides locais | Copiar → `settings.local.json` (gitignored) |
| **commands/** | Slash commands | Fluxos invocados com `/nome` |
| `commands/review.md` | `/review` | Revisor independente (aceite + evidência) |
| `commands/pr.md` | `/pr` | Criar pull request |
| `commands/plano.md` | `/plano` | Planejador: plano com critério de aceite |
| `commands/multiagent.md` | `/multiagent` | Orquestrador: loop intake → entrega |
| `commands/security-check.md` | `/security-check` | Checagem rápida de segurança |
| `commands/api/health-check.md` | `/api.health-check` | Validar rota de health da API fictícia |
| `commands/deploy/staging.md` | `/deploy.staging` | Fluxo de deploy staging (template) |
| **agents/** | Subagents | Especialistas com escopo restrito |
| `agents/intake.md` | Entrada | Briefing e escopo fechado |
| `agents/orchestrator.md` | Orquestrador | Risco, delegação, memória durável |
| `agents/planner.md` | Planejador | Tarefas com aceite |
| `agents/architect.md` | Arquiteto | Desenho, riscos, rollback |
| `agents/engineer.md` | Engenheiro | Artefatos isolados |
| `agents/executor.md` | Executor | Execução + evidências |
| `agents/reviewer.md` | Revisor | Parecer independente |
| `agents/new-feature.md` | Nova feature | Backend, testes e frontend de entidade |
| `agents/security-audit.md` | Auditoria | Auth, inputs, credenciais e privacidade |
| **plans/** | Planos `.plan.md` | Saída do `/plano` e execução multiagente |
| `plans/example-feature.plan.md` | Exemplo export CSV | Plano fictício com fases e todos |
| `plans/example-feature_a1b2c3d4.plan.md` | Exemplo webhooks | Plano fictício com diagrama Mermaid |
| `plans/archive/README.md` | Archive | Preservar planos concluídos ou cancelados |
| `plans/.gitkeep` | Placeholder | Manter pasta `plans/` no git |
| **memory/** | Memória + exemplos | work/durable/log + templates MEMORY |
| `memory/README.md` | Guia memória | Camadas do loop + MEMORY.md Claude |
| `memory/examples/MEMORY.md` | Índice exemplo | Ponteiros para outros arquivos de memória |
| `memory/examples/user-role.md` | Perfil usuário | Papel e preferências do dev |
| `memory/examples/feedback-testing.md` | Feedback testes | Preferências de mock e integração |
| `memory/examples/feedback-commits.md` | Feedback commits | Estilo de mensagem de commit |
| `memory/examples/project-ctx.md` | Contexto projeto | Feature em andamento (fictício) |
| `memory/examples/ref-issue-tracker.md` | Referência externa | Link e convenções do issue tracker |
| **memory-templates/** | Modelos vazios | Base para criar memória local |
| `memory-templates/MEMORY.md` | Template índice | Esqueleto do MEMORY.md (< 200 linhas) |
| `memory-templates/feedback-commits.md` | Template feedback | Registrar aprendizado sobre commits |
