# Vibe Coding com Claude

Esta documentação reúne prompts práticos para orientar desenvolvimento com Claude.

## Prompt base (descoberta e análise)

```text
Quero resolver a seguinte demanda:
[descreva demanda]

Analise o contexto e responda com:
1. entendimento do problema
2. plano mínimo de execução
3. arquivos que provavelmente serão alterados
4. estratégia de validação (testes e verificação manual)
```

## Prompt para codar com segurança

```text
Implemente a solução para:
[tarefa]

Restrições:
- Fazer alterações cirúrgicas.
- Evitar mudanças não relacionadas.
- Manter compatibilidade com comportamento atual.
- Destacar edge cases cobertos.
```

## Prompt para fechamento

```text
Antes de finalizar:
- confira se todos os critérios foram atendidos
- liste os testes executados
- detalhe limitações conhecidas
- apresente um resumo objetivo das mudanças
```
