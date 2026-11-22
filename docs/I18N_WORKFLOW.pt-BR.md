# Fluxo de internacionalização (i18n)

> **Canonical (EN-US):** [I18N_WORKFLOW.md](I18N_WORKFLOW.md)
>
> **Purpose / Para que serve:** Definir como este repositório trata inglês (EN-US) e português (PT-BR) em documentação de governança, regras e comportamento dos agentes.
> **Função:** Estabelecer o fluxo bilíngue do repositório — EN-US como padrão canônico, PT-BR como idioma secundário.

## Visão geral

| Camada | Idioma padrão | Observações |
|--------|---------------|-------------|
| Docs e regras canônicas (voltadas ao agente) | **EN-US** | Conteúdo de governança novo e atualizado |
| Código, commits, docstrings | **Inglês** | Sem mudança — padrão da indústria |
| Chat usuário ↔ agente | **Idioma do usuário** | Acompanhar PT-BR ou EN-US conforme o usuário escreve |
| Docs humanas em PT-BR | **Secundário** | Traduções ou seções PT quando o público no Brasil é prioritário |

Este repositório é um **template de governança**, não uma UI de aplicação. O objetivo é política clara e migração gradual — não duplicar cada arquivo nos dois idiomas.

## Tabela de decisão: quando escrever EN vs PT

| Tipo de conteúdo | Idioma | Justificativa |
|------------------|--------|---------------|
| Novos docs canônicos (`docs/`, guias na raiz) | EN-US | Melhor parsing pelos agentes, reuso mais amplo, alinhado a código/commits |
| Corpo das regras em `.cursor/rules/` (instruções ao agente) | EN-US | Carregado no contexto do modelo a cada sessão |
| Constituição `CLAUDE.md` | EN-US | Claude Code carrega automaticamente |
| Cabeçalhos de regra/arquivo (`Purpose` / `Função`) | One-liner bilíngue | Ajuda mantenedores humanos na transição |
| Corpo principal do README | EN-US (com nota/link PT) | Entrada para público global; linkar tradução PT quando existir |
| Guias longos já em PT-BR | Manter até migrar | Não traduzir em massa; migrar ao tocar ou por prioridade |
| Prompts para times brasileiros | PT-BR OK | Específico de audiência; linkar resumo EN se útil |
| Mensagens de commit, títulos de PR, comentários de código | Inglês | Convenção do time e ferramentas |
| Mensagens de erro em código de API de exemplo | Inglês | Exemplos no estilo produção |

## Nomenclatura de arquivos para traduções

**Convenção (regra única):** sufixo `.pt-BR.md` ao lado do arquivo canônico.

| Canônico (EN-US) | Tradução PT-BR |
|------------------|----------------|
| `README.md` | `README.pt-BR.md` |
| `docs/I18N_WORKFLOW.md` | `docs/I18N_WORKFLOW.pt-BR.md` |
| `PROJECT_GUIDE.md` | `PROJECT_GUIDE.pt-BR.md` |

Regras:

- O **caminho sem sufixo é sempre canônico (EN-US)** após a migração.
- **Não** usar árvore paralela `docs/pt-BR/` — uma convenção só.
- Linkar traduções a partir do doc canônico (topo ou rodapé): `> PT-BR: [Título](path.pt-BR.md)`.
- Se hoje só existir PT, manter o arquivo; adicionar EN na próxima edição substancial ou registrar em [Migração](#estratégia-de-migração).

## Comportamento dos agentes

1. **Comunicação com o usuário:** Responder no idioma que o usuário usa (PT-BR ou EN-US). Se não estiver claro, padrão EN-US.
2. **Docs voltadas ao agente:** Tratar markdown sem sufixo e regras EN-US como autoritativas.
3. **Novo conteúdo de governança:** Escrever em EN-US, salvo tarefa explicitamente para audiência só PT-BR.
4. **Saída de código:** Sempre em inglês (identificadores, docstrings, comentários, mensagens de commit).
5. **Editar docs PT-BR existentes:** Preferir diffs mínimos; ao reescrever em grande escala, separar canônico EN + `.pt-BR.md`.

## O que permanece só em inglês

- Código-fonte, testes, chaves de configuração
- Commits Git e nomes de branch (segmento descritivo em inglês)
- Schemas de API, OpenAPI, campos de request/response de exemplo
- Strings sensíveis à segurança em templates (sem ambiguidade de idioma em fluxos de auth)

## Estratégia de migração

**Não** traduzir em massa guias com 2000+ linhas de uma vez. Use esta ordem:

### Fase 1 — Política (concluída quando este arquivo entrar)

- [x] Publicar `docs/I18N_WORKFLOW.md`
- [x] Atualizar regras core, `CLAUDE.md`, `README.md`, `PROJECT_GUIDE.md`

### Fase 2 — Pontos de entrada de alto tráfego (ao tocar)

| Prioridade | Arquivo | Ação |
|------------|---------|------|
| P0 | `README.md` | Canônico EN + `README.pt-BR.md` quando pronto |
| P0 | `.cursor/rules/core-rules/agent-behavior-always.mdc` | Corpo EN + cabeçalhos bilíngues |
| P1 | `PROJECT_GUIDE.md` | Reescrita EN ou split |
| P1 | `docs/CURSOR_STRUCTURE_GUIDE.md` | EN ao longo do tempo; manter PT até fasear |
| P2 | Docs de prompt (`cursor-vibe-coding-prompts.md`, etc.) | Por audiência; cabeçalhos EN opcionais |

### Fase 3 — Regras e skills

- Novas regras: corpo EN-US, cabeçalho bilíngue `Purpose / Função`.
- Regras PT existentes: migrar quando editadas por outros motivos.

### Fase 4 — Traduções

- Adicionar irmãos `.pt-BR.md` para docs em que leitores brasileiros são prioritários.
- Marcar traduções desatualizadas com linha `Last synced:` apontando para commit ou data do EN.

## Checklist do mantenedor

Ao adicionar ou alterar docs de governança:

- [ ] O arquivo canônico está em EN-US (sem sufixo)?
- [ ] Se o público PT precisa, existe irmão `.pt-BR.md` ou seção?
- [ ] Os links cruzados são bidirecionais (EN ↔ PT)?
- [ ] Cabeçalhos de regra bilíngues para leitura humana?
- [ ] Código/commits ainda em inglês?

## Referências

- Regra core do agente: [.cursor/rules/core-rules/agent-behavior-always.mdc](../.cursor/rules/core-rules/agent-behavior-always.mdc)
- Constituição do projeto: [CLAUDE.md](../CLAUDE.md)
- Índice humano: [PROJECT_GUIDE.md](../PROJECT_GUIDE.md)