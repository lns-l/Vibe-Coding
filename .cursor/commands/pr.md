# /pr

> **Para que serve:** Slash command para fechar o ciclo com PR no GitHub.
> **Função:** Resumir diff, commit/push e criar pull request com descrição estruturada (template).

Cria pull request: commit, push e descrição do diff (template).

## Fluxo
1. `git diff` — entender mudanças
2. Se linter falhou: invocar `/review`
3. Mensagem Conventional Commits
4. `git add` → `git commit` → `git push -u origin HEAD`
5. `gh pr create` com título + body (Summary + Test plan)

## Regras
- Nunca incluir secrets no commit
- Nunca force push sem confirmação explícita
- Nunca PR de `main` para `main`

## Saída
URL do PR criado
