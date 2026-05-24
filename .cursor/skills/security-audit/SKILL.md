# Skill: Security Audit

> **Para que serve:** Checklist de auditoria de segurança reutilizável pelo agente.
> **Função:** Cobrir auth, inputs, credenciais, logs e dependências antes de release ou merge.

## Quando esta skill é relevante
- Antes de releases
- Quando o usuário pede "auditoria de segurança"
- Após novo endpoint ou integração externa

## Checklist

### Autenticação e autorização
- [ ] Endpoints sensíveis protegidos
- [ ] Verificação de role/permissão no lugar correto
- [ ] TTL adequado em tokens

### Validação de inputs
- [ ] Schema validation (não ad-hoc)
- [ ] Limites de tamanho em uploads e campos texto
- [ ] Risco de injection avaliado

### Dados e privacidade
- [ ] PII ausente em logs
- [ ] Responses sem campos desnecessários
- [ ] Sessões em armazenamento seguro

### Infraestrutura
- [ ] Serviços internos não expostos publicamente
- [ ] Dependências com versão fixada

## Como reportar
Formato: `[SEVERIDADE] arquivo:linha — descrição — recomendação`
Severidades: CRÍTICO / ALTO / MÉDIO / BAIXO / INFO
