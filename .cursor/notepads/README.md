# Notepads — Exemplos (template)

> **Para que serve:** Guia dos exemplos de Notepad para contexto volátil no Cursor.
> **Função:** Explicar quando usar `@Notepad` vs rules/skills e listar arquivos de exemplo incluídos.

Notepads são contexto persistente injetado via `@NomeDoNotepad` no chat.
Estes arquivos são **referência** — no Cursor, crie notepads na UI com conteúdo similar.

## Quando usar
- Contexto de sprint ou decisões recentes (muda frequentemente)
- Contratos de API ainda não refletidos no código
- Runbooks de plantão

## Quando NÃO usar
- Padrões estáveis → Rules ou Skills versionadas em git
- Credenciais ou tokens → nunca em notepads

## Exemplos incluídos
- `Sprint_Context.example.md` — objetivos do sprint fictício
- `API_Contract_v2.example.md` — contrato REST de exemplo

Copie o conteúdo para um Notepad no Cursor quando iniciar trabalho relacionado.
