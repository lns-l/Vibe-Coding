# /infra-up

> **Para que serve:** Slash command para subir infra local de desenvolvimento.
> **Função:** Validar pré-requisitos e executar compose/scripts de exemplo (customizar no seu projeto).

Sobe ambiente local de exemplo (template — customize comandos).

## Pré-requisitos
- Docker Desktop em execução (se usar compose)
- `.env` copiado de `.env.example` (valores fictícios OK)

## Fluxo

1. Verificar pré-requisitos (`docker info`, etc.)
2. Executar: `docker compose up -d` (placeholder)
3. Aguardar healthchecks; reportar URLs (ex.: http://localhost:8000/docs)

## Saída
Status por serviço: ✅ up / ❌ failed + logs resumidos

## Regras
- Não expor secrets no chat
- Se falhar: diagnóstico antes de tentar de novo
