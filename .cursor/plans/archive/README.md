# Archive de Planos

> **Para que serve:** Política de arquivamento de planos `.plan.md` concluídos ou cancelados.
> **Função:** Preservar histórico de decisões e execução sem poluir a pasta ativa de planos.

## Quando mover para `archive/`
- Plano concluído com todos os `todo.status = completed`
- Plano cancelado ou substituído
- Plano exploratório que não será executado

## Valor do archive
Planos arquivados são memória institucional — mostram como o time
pensou em problemas anteriores, quais modelos usou e critérios de "pronto".

**Não deletar** — mover com `git mv .cursor/plans/foo.plan.md .cursor/plans/archive/`
