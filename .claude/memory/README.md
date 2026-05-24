# Memory (Claude Code)

> **Para que serve:** Guia da memória persistente entre sessões do Claude Code.
> **Função:** Explicar estrutura em `~/.claude/projects/.../memory/` e apontar para exemplos locais.

Persistência real entre sessões fica em:

```
~/.claude/projects/<nome-do-projeto>/memory/
├── MEMORY.md          # Índice (carregado em toda sessão, < 200 linhas)
├── user-*.md          # type: user
├── feedback-*.md      # type: feedback
├── project-*.md       # type: project
└── ref-*.md           # type: reference
```

Esta pasta contém apenas **exemplos** para copiar/adaptar localmente.  
Não commitar PII, credenciais ou dados de produção.

Ver `docs/CLAUDE_CODE_GUIDE.md` §8 e exemplos em `examples/`.
