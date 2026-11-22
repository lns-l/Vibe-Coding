# Boas Práticas de Produção — FastAPI + LDAP/AD

> **Para que serve:** Referência consolidada de padrões extraídos de um projeto FastAPI+LDAP/AD regulado em produção.
> **Função:** Servir como guia instrutivo para quem adaptar este template a uma aplicação real — sem código real copiado, apenas diretrizes reutilizáveis.

> **Origem:** Análise do projeto AD-WEB-V2 (plataforma IAM corporativa — FastAPI + MongoDB/Beanie + LDAP + React/MUI).
> **Escopo:** Este documento não contém código desse projeto. Tudo aqui é formulado como diretriz genérica.

---

## Sumário

1. [Arquitetura em camadas](#1-arquitetura-em-camadas)
2. [Gerenciamento de configuração (config.env)](#2-gerenciamento-de-configuração-configenv)
3. [Autenticação e JWT](#3-autenticação-e-jwt)
4. [LDAP / Active Directory](#4-ldap--active-directory)
5. [Rate limiting e proteção de endpoints](#5-rate-limiting-e-proteção-de-endpoints)
6. [Segurança de API (FastAPI)](#6-segurança-de-api-fastapi)
7. [Frontend — API centralizada](#7-frontend--api-centralizada)
8. [Docker e infra local](#8-docker-e-infra-local)
9. [Testes](#9-testes)
10. [Auditoria e logs](#10-auditoria-e-logs)
11. [Governança de agentes IA](#11-governança-de-agentes-ia)
12. [Anti-padrões críticos](#12-anti-padrões-críticos)

---

## 1. Arquitetura em camadas

Projetos FastAPI de produção beneficiam de separação clara entre camadas:

| Camada | Responsabilidade | Localização típica |
|--------|-----------------|-------------------|
| **Routers** | HTTP: receber request, validar schema, retornar response | `routers/<domínio>.py` |
| **Services** | Lógica de negócio, orquestração entre connectors | `services/<domínio>_service.py` |
| **Connectors** | Integração com sistemas externos (LDAP, APIs, e-mail) | `connectors/<provedor>/` |
| **Models** | Entidades de persistência (Beanie/SQLAlchemy) | `models/<entidade>.py` |
| **Auth** | JWT, bcrypt, dependencies de role, MFA | `auth/` |
| **Config** | Settings tipadas via pydantic-settings | `config.py` |

**Regra:** Routers não chamam connectors diretamente — passam por services. Isso facilita mocking em testes.

### Schemas Pydantic

Para APIs menores, schemas Pydantic podem viver no arquivo do router (`users.py` define `UserCreate`, `UserResponse`). Para domínios complexos com muitos modelos, criar `schemas/<domínio>.py` separado.

---

## 2. Gerenciamento de configuração (config.env)

### Princípios

1. **Um único arquivo de configuração** por ambiente: `backend/config.env` (git-ignored)
2. **Versionar apenas o exemplo**: `backend/config.env.example` com comentários explicativos
3. **Validação fail-closed no startup**: a aplicação não inicia com configuração inválida

### Estrutura recomendada do config.py

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="config.env",
        env_prefix="BACKEND_",
        extra="ignore",
    )

    jwt_secret: str
    allowed_hosts: list[str] = ["localhost"]
    dev_mode: bool = False
    # ...

settings = Settings()
```

### Resolução de secrets em 3 níveis (prioridade decrescente)

1. Variável de ambiente direta: `BACKEND_JWT_SECRET=<valor>`
2. Arquivo montado (Docker secrets): `BACKEND_JWT_SECRET_FILE=/run/secrets/jwt_secret`
3. Valor criptografado em banco de dados (para rotação dinâmica)

### Validação de startup obrigatória

```python
@app.on_event("startup")
async def validate_runtime_config():
    """Fail loudly on invalid production configuration."""
    if settings.jwt_secret in ("", "changeme", "secret"):
        raise RuntimeError("JWT_SECRET is insecure — set a strong random value")
    if not settings.dev_mode and "*" in settings.allowed_hosts:
        raise RuntimeError("ALLOWED_HOSTS must be explicit in production")
```

---

## 3. Autenticação e JWT

### Cookie httpOnly (padrão recomendado)

JWT em cookie `httpOnly` é mais seguro que `localStorage` pois é inacessível via JavaScript:

- **Backend:** `response.set_cookie(key="access_token", value=jwt, httponly=True, secure=True, samesite="lax")`
- **Frontend:** `axios.create({ withCredentials: true })` — cookie enviado automaticamente

### Diretrizes JWT

| Aspecto | Diretriz |
|---------|----------|
| Segredo | Mínimo 32 bytes aleatórios; validar no startup |
| TTL access token | Curto (15-60 min) |
| Refresh token | Rotação a cada uso; revogar no logout |
| Algoritmo | HS256 mínimo; RS256 para audiências múltiplas |
| Payload | Sem senha, sem PII sensível |

### Anti-enumeração

```
✅ "Invalid credentials"        — não revela se usuário existe
❌ "User not found"              — enumeration attack
❌ "Incorrect password"          — enumeration attack
```

Usar hash dummy (ex.: bcrypt com custo fixo) mesmo para usuários inexistentes para equalizar timing.

---

## 4. LDAP / Active Directory

### Conexão segura

- **Produção:** `ldaps://` (porta 636) ou `ldap://` com STARTTLS (porta 389)
- Validar certificado do servidor (`OPT_X_TLS_DEMAND`) — nunca silenciar erros de cert em produção
- Sempre fechar conexão em bloco `finally` (liberar recursos do pool)

### Sanitização obrigatória — RFC 4515

Todo input de usuário inserido em filtros LDAP **deve** ser escapado:

```
Caracteres especiais: \ → \5c  |  * → \2a  |  ( → \28  |  ) → \29  |  \0 → \00
```

Implementar função `escape_ldap_filter_value(value: str) -> str` e usar em 100% dos casos.

Exemplo de filtro seguro:
```
(&(objectClass=user)(sAMAccountName={escape_ldap_filter_value(username)}))
```

### Bind credentials

- Bind DN e senha LDAP em `config.env` — nunca hardcoded
- Usar conta de serviço com permissões mínimas (apenas leitura para busca)
- Senha de bind deve ser gerada aleatoriamente e armazenada como secret

---

## 5. Rate limiting e proteção de endpoints

### Biblioteca recomendada: slowapi

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
```

### Limites sugeridos por tipo de endpoint

| Tipo | Limite sugerido |
|------|----------------|
| Login | 5 req/min por IP |
| Esqueci a senha | 3 req/min por IP |
| Setup inicial / bootstrap | 3 req/min por IP |
| Endpoints de consulta autenticados | 100 req/min |

### Resposta 429

Retornar mensagem padronizada sem vazar política interna:
```json
{"detail": "Too many requests. Please try again later."}
```

### Middleware de segurança complementar

- **Trusted Host:** validar `Host` header contra `ALLOWED_HOSTS`
- **Security Headers:** `X-Content-Type-Options`, `X-Frame-Options`, `X-XSS-Protection`
- **IP Threat:** bloquear IPs com padrão de ataque (ban exponencial)

---

## 6. Segurança de API (FastAPI)

### Router fail-closed

```python
# Todas as rotas do router exigem autenticação por padrão
router = APIRouter(dependencies=[Depends(get_current_user)])

# Endpoints que precisam de role específica adicionam dependency extra
@router.delete("/{id}", dependencies=[Depends(get_current_admin)])
async def delete_item(id: str): ...
```

### OpenAPI em produção

```python
app = FastAPI(
    docs_url="/docs" if settings.dev_mode else None,
    redoc_url="/redoc" if settings.dev_mode else None,
    openapi_url="/openapi.json" if settings.dev_mode else None,
)
```

### Bootstrap endpoints (uso único)

Endpoints de configuração inicial devem retornar **404 após o primeiro uso** — nunca permanecem ativos em produção:

```python
@router.post("/setup")
async def setup(body: SetupRequest):
    if await db.is_initialized():
        raise HTTPException(404)  # fail-closed após setup
    ...
```

---

## 7. Frontend — API centralizada

### Estrutura de serviços

```
frontend/src/services/
├── core/
│   ├── api.ts           # axios instance autenticada (withCredentials)
│   └── publicApi.ts     # axios sem auth (login, public endpoints)
├── auth/
│   └── index.ts         # authService.me(), authService.logout()
├── users/
│   └── index.ts         # userService.list(), userService.create()
└── types/
    └── index.ts         # Todos os tipos TypeScript centralizados
```

### Configuração do axios

```typescript
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? "/api",
  withCredentials: true,  // envia cookie httpOnly automaticamente
});

// Interceptor: redirecionar para login em 401
api.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      window.location.href = "/login";
    }
    return Promise.reject(err);
  }
);
```

### TypeScript — tipos centralizados

- Um arquivo `types/index.ts` para interfaces que espelham contratos da API
- Nunca usar `any` sem justificativa comentada
- Props de componentes tipadas explicitamente

---

## 8. Docker e infra local

### Dockerfile backend (Python)

```dockerfile
FROM python:3.12-slim

# System deps para python-ldap (se aplicável)
RUN apt-get update && apt-get install -y \
    libldap2-dev libsasl2-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Non-root user obrigatório
RUN useradd -m appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile frontend (multi-stage)

```dockerfile
# Stage 1: build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: serve
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
```

### docker-compose — isolamento de portas

| Serviço | Exposição recomendada |
|---------|----------------------|
| Frontend (Nginx) | `3000:80` — único ponto de entrada |
| Backend (FastAPI) | Apenas `expose` — sem porta no host |
| Banco de dados | Apenas `expose` — sem porta no host |
| Cache (Redis) | Apenas `expose` — sem porta no host |

### Docker Secrets

```yaml
secrets:
  encryption_key:
    file: ./secrets/encryption_key
services:
  backend:
    secrets: [encryption_key]
    environment:
      BACKEND_ENCRYPTION_KEY_FILE: /run/secrets/encryption_key
```

---

## 9. Testes

### Setup pytest assíncrono

`pyproject.toml`:
```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"

[tool.coverage.report]
fail_under = 50   # gate de CI; meta real: 70% por módulo
```

### Fixture de client (httpx ASGITransport)

```python
# conftest.py
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as c:
        yield c
```

### Mocking de LDAP

```python
from unittest.mock import patch, MagicMock

@patch("app.connectors.ldap.connector.ldap.initialize")
async def test_search_user(mock_ldap_init, client):
    mock_conn = MagicMock()
    mock_ldap_init.return_value = mock_conn
    mock_conn.search_s.return_value = [("cn=user,dc=corp,dc=com", {"sAMAccountName": [b"user"]})]
    # ... teste da lógica sem LDAP real
```

### Auth surface gate

Teste que percorre todos os prefixos protegidos e garante que retornam 401 sem autenticação — executar em pre-commit como gate de segurança:

```python
PROTECTED_PREFIXES = ["/api/users", "/api/admin"]

async def test_protected_endpoints_require_auth(client):
    for prefix in PROTECTED_PREFIXES:
        r = await client.get(f"{prefix}/")
        assert r.status_code in (401, 403, 404), f"{prefix} should require auth"
```

---

## 10. Auditoria e logs

### Campos mínimos de log de auditoria

| Campo | Obrigatório | Notas |
|-------|-------------|-------|
| `actor_id` | ✅ | ID do usuário autenticado |
| `actor_role` | ✅ | Role no momento da ação |
| `action` | ✅ | Ação descritiva (ex.: `user.create`) |
| `resource_type` | ✅ | Tipo do recurso afetado |
| `resource_id` | ✅ | ID do recurso |
| `outcome` | ✅ | `success` ou `failure` |
| `timestamp` | ✅ | UTC |
| `trace_id` | Recomendado | Para correlação de logs |
| `changes` | Para mutações | `[{field, before, after}]` |

### Regras de log

- Auditoria nunca deve bloquear a operação principal — usar `try/except` local isolado
- **Nunca** incluir no log: senhas, tokens, chaves, dados PII sensíveis
- Ações visíveis ao usuário final devem ter label correspondente no frontend

---

## 11. Governança de agentes IA

### Princípio: `.cursor/` como fonte de verdade

- `CLAUDE.md` aponta para `.cursor/agents/` e `.cursor/skills/` — não duplica conteúdo
- Rules `alwaysApply` devem ser curtas (< 50 linhas); detalhes longos em Skills (sob demanda)
- Skills de operações críticas (LDAP, AD, auditoria regulatória) devem ser agent-requestable, não always-apply

### Rules por glob vs alwaysApply

| Tipo | Uso ideal |
|------|-----------|
| `alwaysApply: true` | Segurança baseline, idioma, escopo — curto |
| Glob (`globs:`) | Padrões específicos de stack (routers, testes, docker) |
| Agent requested | Skills longas, operações raras, integrations complexas |

### Paralelismo seguro de subagents

Nunca paralelizar subagents que editam simultaneamente:
- `main.py` / `config.py` / `auth/`
- `frontend/src/services/core/api.ts`
- `docker-compose.yml`

Para refatorações grandes (5+ arquivos): criar plano em `.cursor/plans/` antes de executar.

---

## 12. Anti-padrões críticos

| Anti-padrão | Risco | Correção |
|-------------|-------|----------|
| Input LDAP sem escape | LDAP Injection → acesso não autorizado | `escape_ldap_filter_value()` obrigatório |
| JWT em `localStorage` | XSS rouba token | Cookie `httpOnly` + `withCredentials` |
| Mensagem de auth específica | Enumeration de usuários | Mensagem genérica sempre |
| Endpoint auth sem rate limit | Brute force | slowapi com limite por IP |
| `except:` vazio em auth | Falha silenciosa | Log + reraise ou HTTPException |
| OpenAPI em produção | Expõe contratos internos | `docs_url=None` fora de dev mode |
| Bind LDAP hardcoded | Credential leak | `config.env` + Docker secrets |
| Tag `:latest` em Docker | Builds não-reproduzíveis | Tag semântica ou digest |
| Backend rodando como root | Escalação de privilégio | `USER appuser` no Dockerfile |
| Portas internas expostas no host | Acesso direto ao banco/cache | Apenas `expose` no compose |
