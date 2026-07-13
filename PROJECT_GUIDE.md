# PROJECT_GUIDE.md (template)

> **Para que serve:** Índice humano do projeto — stack de exemplo, segurança e links para configuração de IA.
> **Função:** Complementar [CLAUDE.md](CLAUDE.md) e `.cursor/rules/` com visão de produto e onboarding rápido.

> Ponto de entrada humano para o projeto. Para agentes no **Claude Code**, a fonte autoritativa é [CLAUDE.md](CLAUDE.md).
> Para **Cursor**, use `.cursor/rules/` e este arquivo como visão geral.

## Objetivo

Repositório **Vibe-Coding**: base de comparação entre governança de IA no Cursor (`.cursor/`) e no Claude Code (`.claude/` + `CLAUDE.md`).

## Stack de exemplo (fictícia)

| Camada | Tecnologia |
|--------|------------|
| API | Python 3.12, FastAPI |
| Frontend | TypeScript, React |
| Dados | PostgreSQL (dev only) |
| Auth | JWT em cookie httpOnly, bcrypt |
| Diretório (opcional) | LDAP / Active Directory via python-ldap |
| Config | `config.env` + `config.py` (pydantic-settings) |

## Onde configurar cada ferramenta

| Ferramenta | Configuração |
|------------|----------------|
| Cursor | [.cursor/](.cursor/) — rules, hooks, MCP, agents |
| Claude Code | [CLAUDE.md](CLAUDE.md) + [.claude/](.claude/) |

## Segurança (não negociável)

- Sem secrets reais neste template
- Copie `mcp.env.example` → `mcp.env` (local, gitignored) apenas no seu fork
- Variáveis documentadas em `.env.example`

## Documentação

| Arquivo | Função |
|---------|--------|
| [README.md](README.md) | Entrada do repo e mapa completo |
| [docs/I18N_WORKFLOW.md](docs/I18N_WORKFLOW.md) · [PT-BR](docs/I18N_WORKFLOW.pt-BR.md) | Fluxo bilíngue: EN-US canônico, PT-BR secundário, convenção `.pt-BR.md` |
| [docs/cursor-vibe-coding-prompts.md](docs/cursor-vibe-coding-prompts.md) | Prompts para Cursor |
| [docs/claude-vibe-coding-prompts.md](docs/claude-vibe-coding-prompts.md) | Prompts para Claude |
| [docs/CURSOR_STRUCTURE_GUIDE.md](docs/CURSOR_STRUCTURE_GUIDE.md) | Guia detalhado `.cursor/` |
| [docs/CLAUDE_CODE_GUIDE.md](docs/CLAUDE_CODE_GUIDE.md) | Guia detalhado `.claude/` |
| [docs/BEST_PRACTICES_FROM_PRODUCTION.md](docs/BEST_PRACTICES_FROM_PRODUCTION.md) | Boas práticas de produção (FastAPI + LDAP/AD) |
| [docs/I18N_WORKFLOW.md](docs/I18N_WORKFLOW.md) · [PT-BR](docs/I18N_WORKFLOW.pt-BR.md) | Política bilíngue EN-US (canônico) + PT-BR (secundário) |
| [.cursor/README.md](.cursor/README.md) | Catálogo da estrutura Cursor |
| [.claude/README.md](.claude/README.md) | Catálogo da estrutura Claude |
