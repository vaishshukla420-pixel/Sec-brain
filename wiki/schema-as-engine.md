---
title: Schema as Engine
date: 2026-07-11
type: concept
source: raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf
tags: [knowledge-systems, ai]
---

**A schema file the agent reads at the start of every session turns ad-hoc AI
assistance into a reproducible system — the schema is the system's source
code.**

Claude Code loads `CLAUDE.md` automatically each session. Because the schema
defines the operations of the [[second-brain-loop]] precisely — what ingest
does step by step, how queries cite, what lint may and may not touch — the
system behaves consistently across sessions, machines, and even models, and
never has to be re-explained. Karpathy calls this file the schema; it is the
difference between "an AI that helps with my notes" and "a system."

Two properties follow from treating the schema as source code:

- **It's versioned.** The schema lives in git, so process changes are
  diffable, reviewable, and reversible — the system's own history is auditable.
- **It carries the guardrails.** Report-don't-delete linting
  ([[wiki-linting]]), commit-per-operation, and the untrusted-input rule are
  encoded in the spec, not left to the model's judgment on the day.

## Links

- [[second-brain-loop]] — the loop the schema specifies
- [[connection-maintenance]] — the schema's search-first rule keeps linking viable at scale
- [[wiki-linting]] — guardrails live in the schema, lint enforces the rest

## Source

- Guide: `raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf`
- Upstream: Andrej Karpathy, "LLM Knowledge Bases" —
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
