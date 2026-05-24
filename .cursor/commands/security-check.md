# /security-check

> **Para que serve:** Slash command de auditoria rápida de segurança.
> **Função:** Verificar credenciais, validação de input e rotas sensíveis no diff (template).

Auditoria rápida de segurança no diff atual (template).

## Verificações

### Credenciais
- Strings que parecem tokens/senhas literais
- `.env` ou configs sensíveis staged

### Auth
- Rotas sensíveis com autenticação e autorização
- Tokens em armazenamento seguro

### Inputs e outputs
- Validação de schema antes de usar dados externos
- PII/credenciais ausentes em logs

### Dependências
- Versões fixadas em pacotes novos

## Saída
Relatório: ✅ OK / ⚠️ Atenção / ❌ Crítico por categoria

## Regras
- Invocar skill `@security-audit` para checklist completo
- Não modificar código sem aprovação
