# Guia de Seleção de Modelos (template)

> **Para que serve:** Política de escolha de modelo/tier no Cursor para este template.
> **Função:** Indicar quando usar tier econômico vs thinking e como escalar só com evidência de falha.

## Princípio
Use o **menor tier** que entregue qualidade aceitável. Suba apenas com evidência de falha.

## Quando usar Auto/Composer
- Edição em 1 arquivo com instrução clara
- Formatação, imports, rename
- Perguntas sobre código existente

## Tabela de seleção

| Complexidade | Tier sugerido |
|--------------|---------------|
| Edição mecânica em 1 arquivo | Econômico |
| Refactor multi-arquivo com padrão claro | Econômico-médio |
| Consolidação com lógica moderada | Médio |
| Design com dependências cruzadas | Médio-alto + thinking |
| Segurança, auth, compliance | Alto |
| Parent de plano com 8+ fases | Alto + thinking |

## Thinking — quando usar
- Decisões com 2+ opções não óbvias
- Análise de impacto em módulo crítico
- Máximo ~2 fases thinking por plano
- Evitar thinking em fases mecânicas

## Escalada
1. Começar com Auto / Composer
2. Falhou? → Subir um tier + contexto explícito
3. Documentar motivo no plano
