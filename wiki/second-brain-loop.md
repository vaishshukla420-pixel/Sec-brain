---
title: Second Brain Loop
date: 2026-07-11
type: hub
source: raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf
tags: [knowledge-systems]
---

**A knowledge base compounds only when it runs a closed loop — ingest, query,
lint — instead of merely accumulating notes.**

Storage systems get bigger; loop systems get smarter. The difference is what
happens after capture:

- **Ingest** — a source is broken into [[atomic-notes]] and integrated:
  linked against what is already here, indexed, logged.
- **Query** — questions are answered from the compiled structure, and answers
  worth keeping are filed back as new pages. The output becomes input.
- **Lint** — periodic health checks catch contradictions, superseded claims,
  orphans, and gaps ([[wiki-linting]]). This is the operation everyone skips,
  and the one that keeps the system trustworthy.

The loop's closing move is asking the vault what is missing: gaps identified
during query or lint become the next sources to ingest, so the system steers
its own growth. A vault without the loop is a graveyard with a nice graph view.

## Links

- [[compiled-knowledge-vs-rag]] — why compiling beats re-searching every question
- [[atomic-notes]] — the unit the loop operates on
- [[connection-maintenance]] — why the loop needs an agent to run it
- [[wiki-linting]] — the maintenance half of the loop
- [[schema-as-engine]] — the spec that makes the loop reproducible across sessions

## Source

- Guide: `raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf`
- Upstream: Andrej Karpathy, "LLM Knowledge Bases" —
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
