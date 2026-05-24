# Protocolo de Paralelismo Seguro (template)

> **Para que serve:** Regras para executar múltiplos subagents sem conflito de arquivos.
> **Função:** Listar paths críticos, combinações seguras e checklist antes de paralelizar fases.

## Regra fundamental
Paralelize **apenas** quando os conjuntos de arquivos forem **disjuntos**.

## Arquivos críticos — nunca em paralelo
Substitua pelos paths reais do seu projeto:

| Arquivo | Motivo |
|---------|--------|
| `src/main.py` | Registro de routers e middlewares |
| `src/config/settings.py` | Config central e env loading |
| `src/dependencies.py` | Injeção de dependências |
| `src/middleware/auth.py` | Auth global |
| `docker-compose.yml` | Orquestração de infra |

## Combinações seguras
- ✅ Backend (`src/routers/`) ↔ Frontend (`src/pages/`)
- ✅ Testes novos ↔ código fonte (sem editar source)
- ⚠️ Dois módulos backend — verificar imports compartilhados
- ❌ Qualquer fase ↔ ponto de entrada (`main.py`)
- ❌ Qualquer fase ↔ config central

## Checklist pré-paralelo
- [ ] Arquivos das fases são disjuntos?
- [ ] Nenhuma fase toca arquivo crítico em paralelo?
- [ ] Cada agente tem contexto suficiente?
- [ ] Ordem de merge após paralelo está clara?

## Exemplo de conflito

```
F1: src/models/user.ts, src/schemas/user.ts
F2: src/pages/UserPage.tsx
→ Interseção vazia ✅

F3: src/routes/users.ts, src/app.ts
F4: src/routes/groups.ts, src/app.ts
→ Interseção: src/app.ts ❌ serializar F3 e F4
```
