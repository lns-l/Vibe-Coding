# /review

> **Para que serve:** Slash command de revisão pré-commit no Cursor.
> **Função:** Rodar lint, segurança e checklist de qualidade sobre o diff atual (template).

Revisa mudanças não commitadas com verificações de qualidade do projeto (template).

## Fluxo

### Linters e formatação
1. Executar linter(s) configurados
2. Verificar formatação e imports não utilizados

### Segurança
1. Credenciais hardcoded no diff?
2. Inputs externos validados?
3. Rotas sensíveis protegidas?
4. Arquivos sensíveis staged?

### Consistência
1. Tipos/schemas alinhados com existentes?
2. Naming conforme convenções?
3. Testes para casos novos?

## Saída
Sumário por categoria: ✅ OK / ⚠️ Atenção / ❌ Crítico

## Regras
- Não corrigir automaticamente — aguardar aprovação
- Se linter falhar: exibir output completo
