# Acme API — CLAUDE.md (template)

> **Para que serve:** Constituição do projeto carregada automaticamente pelo Claude Code em cada sessão.
> **Função:** Definir stack, padrões de código, segurança, arquivos críticos e anti-padrões — substitua placeholders pelo seu projeto real.

> Constituição do projeto para Claude Code. Substitua placeholders pelo seu stack real.
> Conteúdo longo ou volátil → commands ou memória (`~/.claude/projects/<proj>/memory/`).

<!--
Changelog:
- 2026-05-24: Template inicial para repositório Vibe-Coding (comparação Cursor vs Claude)
- 2026-07-13: Padrões de produção importados de projeto FastAPI+LDAP/AD real (AD-WEB-V2)
-->

## Visão geral

API REST fictícia **Acme API** (Python/FastAPI + TypeScript/React). Domínio de exemplo: catálogo de itens e integrações webhook. Sem dados reais ou credenciais neste repositório.

## Arquitetura (exemplo)

```
backend/app/
├── main.py           # Entrypoint, middlewares, registro de routers — arquivo crítico
├── config.py         # Settings via pydantic-settings (lê config.env)
├── auth/             # JWT, bcrypt, dependencies de role
├── routers/          # Endpoints por domínio
├── services/         # Lógica de negócio
├── models/           # Entidades / ODM
├── connectors/       # Integrações externas (LDAP, APIs)
└── utils/            # Helpers: criptografia, sanitização de inputs

frontend/src/
├── services/core/api.ts  # Cliente HTTP centralizado — arquivo crítico
├── services/             # Módulos por domínio (auth/, users/, …)
├── types/index.ts        # Todos os tipos TypeScript centralizados
├── pages/                # Telas
└── components/           # UI reutilizável
```

### Configuração de secrets

Projetos reais usam `backend/config.env` (git-ignored) lido por `config.py` via `pydantic-settings`:
- Variáveis com prefixo consistente (ex.: `BACKEND_*`)
- Alternativa via `*_FILE` apontando para Docker secrets montados
- Nunca hardcode em código ou compose — sempre via `env_file`
- Versionar apenas `config.env.example` com comentários descritivos

## Comandos essenciais (placeholders)

- Build: `npm run build` (frontend) / `pip install -e .` (backend)
- Testes: `pytest tests/ -x` / `npm test`
- Lint: `npm run lint` / `ruff check src`
- Validação completa: `./scripts/validate.sh` (criar no seu projeto)

## Padrões de código (few-shot)

### Endpoint (FastAPI)

```python
# ✅ Correto — auth no router, response_model, schema Pydantic
router = APIRouter(dependencies=[Depends(get_current_user)])  # fail-closed

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

### Endpoint de autenticação com rate limiting

```python
# ✅ Correto — rate limit em auth, mensagem genérica, timing constante
@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
async def login(request: Request, body: LoginRequest) -> TokenResponse:
    user = await auth_service.authenticate(body.username, body.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return TokenResponse(access_token=create_jwt(user))

# ❌ Errado — sem rate limit, revela existência do usuário
@router.post("/login")
async def login(body: dict):
    user = await db.find_one({"email": body["email"]})
    if not user:
        raise HTTPException(401, detail="User not found")  # enumeration!
```

### LDAP / Active Directory

```python
# ✅ Correto — sanitização obrigatória antes de qualquer filtro LDAP
from app.connectors.ldap.filters import escape_ldap_filter_value

async def search_user(username: str) -> dict | None:
    safe = escape_ldap_filter_value(username)        # previne LDAP injection
    ldap_filter = f"(&(objectClass=user)(sAMAccountName={safe}))"
    return await ldap_connector.search(ldap_filter)

# ❌ Errado — input não sanitizado → LDAP injection
async def search_user(username: str):
    return await ldap_connector.search(f"(sAMAccountName={username})")
```

### Frontend — API centralizada

```typescript
// ✅ Correto — api.ts centralizado, withCredentials para cookie JWT, tipos explícitos
// services/core/api.ts
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? "/api",
  withCredentials: true,  // httpOnly cookie — nunca expor JWT em localStorage
});

// services/auth/index.ts
export const authService = {
  me: (): Promise<User> => api.get("/auth/me").then((r) => r.data),
  logout: (): Promise<void> => api.post("/auth/logout").then(() => undefined),
};

// ❌ Errado — fetch solto, token em localStorage, any
export async function getUser(): Promise<any> {
  return fetch("/api/me", {
    headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
  }).then((r) => r.json());
}
```

## Regras críticas de segurança

- **Nunca** hardcode tokens, senhas ou API keys — use `config.env` / `config.py`
- **Nunca** commitar `.env`, `config.env`, `mcp.env` ou arquivos com secrets reais
- Validar inputs externos com schema (Pydantic/Zod) antes de usar
- Endpoints sensíveis exigem autenticação (`Depends(get_current_user)`)
- **Sanitizar inputs LDAP** com escape RFC 4515 antes de montar filtros (`escape_ldap_filter_value`)
- **Rate limiting** obrigatório em endpoints de autenticação (ex.: 5 req/min no login)
- **LDAP/AD:** usar TLS (`ldaps://` ou STARTTLS) em produção; nunca plaintext
- Logs sem PII, sem `secret`, sem tokens
- Mensagens de erro de auth genéricas — não revelar existência de usuário/recurso

## Git e commits

- Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, etc.
- Branches: `feature/<nome>`, `fix/<nome>`
- Não commitar: `.env*`, `mcp.env`, `settings.local.json`, `CLAUDE.local.md`

## Arquivos críticos (nunca editar em paralelo)

- `backend/app/main.py` — registro de routers e middlewares
- `backend/app/config.py` — settings e validação de startup (fail-closed em produção)
- `backend/app/auth/` — JWT, bcrypt, dependencies de role
- `backend/app/connectors/` — integrações LDAP/AD/externas
- `frontend/src/services/core/api.ts` — cliente HTTP base com interceptors
- `docker-compose.yml` — orquestração local

## Anti-padrões proibidos

- Credenciais em código ou em JSON versionado
- Input LDAP sem sanitização (`escape_ldap_filter_value`) — vulnerabilidade de injection
- Token JWT em `localStorage` — usar cookie `httpOnly` com `withCredentials`
- Mensagem de auth que revele existência de usuário/email (timing attack / enumeration)
- Endpoint de auth sem rate limiting
- `except:` vazio em fluxos críticos
- `rm -rf` ou operações destrutivas em infra sem confirmação explícita
- MCP de banco apontando para produção
- OpenAPI habilitado em produção (`docs_url=None` fora de dev mode)
- Paralelizar subagents em fases que compartilham os arquivos críticos acima

## Referências neste repo

- Estrutura Claude: [.claude/](.claude/)
- Commands: `.claude/commands/` (`/review`, `/pr`, `/plano`, …)
- Guia completo: [docs/CLAUDE_CODE_GUIDE.md](docs/CLAUDE_CODE_GUIDE.md)
