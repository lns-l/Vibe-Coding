# Internationalization (i18n) Workflow

> **PT-BR:** [Fluxo de internacionalização (i18n)](I18N_WORKFLOW.pt-BR.md)

> **Purpose:** Define how this repository handles English (EN-US) and Portuguese (PT-BR) across governance docs, rules, and agent behavior.
> **Função:** Estabelecer o fluxo bilíngue do repositório — EN-US como padrão canônico, PT-BR como idioma secundário.

## Overview

| Layer | Default language | Notes |
|-------|------------------|-------|
| Canonical docs & rules (agent-facing) | **EN-US** | New and updated governance content |
| Code, commits, docstrings | **English** | Unchanged — industry standard |
| User ↔ agent chat | **User's language** | Match PT-BR or EN-US as the user writes |
| PT-BR human docs | **Secondary** | Translations or PT-first sections where the Brazil audience is primary |

This repo is a **governance template**, not an application UI. The goal is a clear policy and gradual migration — not duplicating every file in both languages.

## Decision table: when to write EN vs PT

| Content type | Language | Rationale |
|--------------|----------|-----------|
| New canonical docs (`docs/`, root guides) | EN-US | Better agent parsing, broader reuse, aligns with code/commits |
| `.cursor/rules/` body text (agent instructions) | EN-US | Loaded into model context every session |
| `CLAUDE.md` constitution | EN-US | Claude Code loads this automatically |
| Rule/file headers (`Purpose` / `Função`) | Bilingual one-liner | Helps human maintainers during transition |
| README primary body | EN-US (with PT note/link) | Entry point for global audience; link PT translation when it exists |
| Long guides already in PT-BR | Keep until migrated | Do not mass-translate; migrate on touch or by priority |
| Prompts for Brazilian teams | PT-BR OK | Audience-specific; cross-link EN summary if useful |
| Commit messages, PR titles, code comments | English | Team convention and tooling |
| Error messages in example API code | English | Production-style examples |

## File naming for translations

**Convention (single rule):** suffix `.pt-BR.md` next to the canonical file.

| Canonical (EN-US) | PT-BR translation |
|-------------------|-------------------|
| `README.md` | `README.pt-BR.md` |
| `docs/I18N_WORKFLOW.md` | `docs/I18N_WORKFLOW.pt-BR.md` |
| `PROJECT_GUIDE.md` | `PROJECT_GUIDE.pt-BR.md` |

Rules:

- The **unsuffixed path is always canonical (EN-US)** once migrated.
- Do **not** use a parallel `docs/pt-BR/` tree — one convention only.
- Link translations from the canonical doc (top or footer): `> PT-BR: [Title](path.pt-BR.md)`.
- If only PT exists today, keep the file; add EN on next substantive edit or track in [Migration](#migration-strategy).

## Agent behavior

1. **User communication:** Reply in the language the user uses (PT-BR or EN-US). If unclear, default to EN-US.
2. **Agent-facing docs:** Treat unsuffixed markdown and EN-US rules as authoritative.
3. **New governance content:** Write in EN-US unless the task explicitly targets a PT-BR-only audience.
4. **Code output:** Always English (identifiers, docstrings, comments, commit messages).
5. **Editing existing PT-BR docs:** Prefer minimal diffs; add EN canonical + `.pt-BR.md` split when doing a major rewrite.

## What stays English only

- Source code, tests, configuration keys
- Git commits and branch names (descriptive segment in English)
- API schemas, OpenAPI, example request/response fields
- Security-sensitive strings in templates (no mixed-language ambiguity in auth flows)

## Migration strategy

Do **not** mass-translate 2000+ line guides in one pass. Use this order:

### Phase 1 — Policy (done when this file lands)

- [x] Publish `docs/I18N_WORKFLOW.md`
- [x] Update core rules, `CLAUDE.md`, `README.md`, `PROJECT_GUIDE.md`

### Phase 2 — High-traffic entry points (on touch)

| Priority | File | Action |
|----------|------|--------|
| P0 | `README.md` | EN canonical + `README.pt-BR.md` when ready |
| P0 | `.cursor/rules/core-rules/agent-behavior-always.mdc` | EN body + bilingual headers |
| P1 | `PROJECT_GUIDE.md` | EN rewrite or split |
| P1 | `docs/CURSOR_STRUCTURE_GUIDE.md` | EN over time; keep PT until phased |
| P2 | Prompt docs (`cursor-vibe-coding-prompts.md`, etc.) | Audience-specific; optional EN headers |

### Phase 3 — Rules and skills

- New rules: EN-US body, bilingual `Purpose / Função` header.
- Existing PT rules: migrate when edited for other reasons.

### Phase 4 — Translations

- Add `.pt-BR.md` siblings for docs where Brazilian readers are primary.
- Mark stale translations with a `Last synced:` line pointing to the EN commit or date.

## Maintainer checklist

When adding or changing governance docs:

- [ ] Is the canonical file EN-US (unsuffixed)?
- [ ] If PT audience needs it, is there a `.pt-BR.md` sibling or section?
- [ ] Are cross-links bidirectional (EN ↔ PT)?
- [ ] Are rule headers bilingual for human scan?
- [ ] Code/commits still English?

## References

- Core agent rule: [.cursor/rules/core-rules/agent-behavior-always.mdc](../.cursor/rules/core-rules/agent-behavior-always.mdc)
- Project constitution: [CLAUDE.md](../CLAUDE.md)
- Human index: [PROJECT_GUIDE.md](../PROJECT_GUIDE.md)
