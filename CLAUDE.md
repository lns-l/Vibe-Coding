# Acme API — CLAUDE.md (template)

> **Para que serve:** Constituição do projeto carregada automaticamente pelo Claude Code em cada sessão.
> **Função:** Definir stack, padrões de código, segurança, arquivos críticos e anti-padrões — substitua placeholders pelo seu projeto real.

> Constituição do projeto para Claude Code. Substitua placeholders pelo seu stack real.
> Conteúdo longo ou volátil → commands ou memória (`~/.claude/projects/<proj>/memory/`).

<!--
Changelog:
- 2026-05-24: Template inicial para repositório Vibe-Coding (comparação Cursor vs Claude)
-->

## Visão geral

API REST fictícia **Acme API** (Python/FastAPI + TypeScript/React). Domínio de exemplo: catálogo de itens e integrações webhook. Sem dados reais ou credenciais neste repositório.

## Arquitetura (exemplo)

```
src/
├── models/       # Documentos / entidades
├── schemas/      # Request/response Pydantic
├── services/     # Lógica de negócio
├── routers/      # Endpoints FastAPI
└── main.py       # Entrypoint — arquivo crítico

frontend/src/
├── services/     # Chamadas HTTP via api.ts
├── pages/        # Telas
└── components/   # UI reutilizável
```

## Comandos essenciais (placeholders)

- Build: `npm run build` (frontend) / `pip install -e .` (backend)
- Testes: `pytest tests/ -x` / `npm test`
- Lint: `npm run lint` / `ruff check src`
- Validação completa: `./scripts/validate.sh` (criar no seu projeto)

## Padrões de código (few-shot)

### Endpoint (FastAPI)

```python
# ✅ Correto — validação + wrapper
@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(
    body: ItemCreate,
    user: User = Depends(get_current_user),
) -> ItemResponse:
    item = await item_service.create(body, actor_id=user.id)
    return ItemResponse.model_validate(item)

# ❌ Errado — req.body cru, sem auth, sem response_model
@router.post("/")
async def create_item(request):
    return await db.items.insert_one(request.json())
```

### Frontend (TypeScript)

```typescript
// ✅ Correto — api centralizado, tipos explícitos
export async function listItems(): Promise<ApiResponse<Item[]>> {
  const { data } = await api.get<ApiResponse<Item[]>>("/items/");
  return data;
}

// ❌ Errado — fetch solto, any
export async function listItems(): Promise<any> {
  return fetch("/items/").then((r) => r.json());
}
```

## Regras críticas de segurança

- **Nunca** hardcode tokens, senhas ou API keys — use variáveis de ambiente
- **Nunca** commitar `.env`, `mcp.env` ou arquivos com secrets reais
- Validar inputs externos com schema (Pydantic/Zod) antes de usar
- Endpoints sensíveis exigem autenticação (`Depends(get_current_user)`)
- Logs sem PII, sem `secret`, sem tokens

## Git e commits

- Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, etc.
- Branches: `feature/<nome>`, `fix/<nome>`
- Não commitar: `.env*`, `mcp.env`, `settings.local.json`, `CLAUDE.local.md`

## Arquivos críticos (nunca editar em paralelo)

- `src/main.py` — registro de routers
- `src/dependencies.py` — DI / auth
- `frontend/src/core/api.ts` — cliente HTTP base
- `docker-compose.yml` — orquestração local

## Anti-padrões proibidos

- Credenciais em código ou em JSON versionado
- `except:` vazio em fluxos críticos
- `rm -rf` ou operações destrutivas em infra sem confirmação explícita
- MCP de banco apontando para produção
- Paralelizar subagents em fases que compartilham os arquivos acima

## Referências neste repo

- Estrutura Claude: [.claude/](.claude/)
- Commands: `.claude/commands/` (`/review`, `/pr`, `/plano`, …)
- Guia completo: [docs/CLAUDE_CODE_GUIDE.md](docs/CLAUDE_CODE_GUIDE.md)
