---
title: Compiled Knowledge vs RAG
date: 2026-07-11
type: concept
source: raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf
tags: [knowledge-systems, ai]
---

**RAG re-derives answers from raw documents on every question and forgets;
a compiled wiki integrates knowledge once and maintains it, so every answer
starts half-built.**

RAG's cycle is ask → retrieve → answer → forget. Nothing accumulates: the
next question starts from zero against the same pile of documents. The
knowledge is searched over and over but never *compiled*.

The wiki approach reads a source once, integrates it into structured pages,
and links it to everything already present. Answers come from the compiled
structure — and can be filed back into it, which is what turns retrieval into
a [[second-brain-loop]]. Karpathy's frame: Obsidian is the IDE, the LLM is
the programmer, the wiki is the codebase — maintained like software, not
searched like a folder.

The honest trade-off: compilation moves cost from read time to write time.
Ingestion is slower than dropping a file into a RAG index, and the compiled
structure needs deliberate upkeep ([[wiki-linting]]) or it rots.

## Links

- [[second-brain-loop]] — the cycle that makes compilation pay off
- [[atomic-notes]] — the unit of compilation
- [[wiki-linting]] — the maintenance cost compilation takes on

## Source

- Guide: `raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf`
- Upstream: Andrej Karpathy, "LLM Knowledge Bases" —
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
