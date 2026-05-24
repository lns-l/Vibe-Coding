# Vibe Coding no Cursor

Esta documentação reúne prompts práticos para orientar o desenvolvimento com a plataforma Cursor.

## Prompt base (planejamento)

```text
Atue como meu par-programador.

Contexto do projeto:
- [descreva objetivo, stack e restrições]

Tarefa:
- [descreva a funcionalidade]

Requisitos:
- Proponha um plano em passos curtos.
- Liste riscos e edge cases.
- Sugira testes antes de implementar.
- Implemente com mudanças mínimas e objetivas.
```

## Prompt para implementação

```text
Implemente a tarefa abaixo com foco em mudanças pequenas e seguras:

[tarefa]

Critérios:
1. Não alterar arquivos fora do escopo.
2. Reaproveitar padrões já existentes no repositório.
3. Criar/ajustar testes necessários.
4. Explicar rapidamente o que foi alterado.
```

## Prompt para revisão

```text
Revise o código gerado e retorne:
- possíveis bugs
- riscos de segurança
- melhorias de legibilidade/manutenção
- pontos de regressão

No fim, traga um checklist de correções priorizadas.
```
