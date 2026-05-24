# @API_Contract_v2 (exemplo fictício)

> **Para que serve:** Modelo de contrato de API ainda não refletido no código.
> **Função:** Documentar endpoints e schemas para o agente alinhar implementação (fictício).

Contrato REST **proposto** — ainda não implementado no código.

## Base URL
`/api/v2`

## Widgets

### GET /widgets/
- Auth: Bearer JWT
- Query: `page`, `limit` (default 20)
- Response: `{ success, data: Widget[], meta: { page, limit } }`

### POST /widgets/
- Auth: Admin
- Body: `{ name, sku, is_active? }`
- 201: `{ success, data: WidgetResponse }`
- 422: validação (SKU duplicado, name vazio)

### WidgetResponse (nunca incluir campos internos)
```json
{
  "id": "uuid",
  "name": "string",
  "sku": "string",
  "is_active": true,
  "created_at": "ISO8601"
}
```

## Notas
- v1 permanece em `/api/v1` até deprecação formal
- Breaking change: wrapper `{ success, data }` obrigatório em v2
