---
title: Wiki Linting
date: 2026-07-11
type: concept
source: raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf
tags: [knowledge-systems]
---

**Without periodic linting a growing vault rots — contradictions accumulate,
claims go stale, pages orphan — and a brain you stop trusting is a brain you
stop using.**

Entropy creeps into any growing wiki in predictable ways: two pages come to
contradict each other; a claim filed in March is superseded by something read
in June but the old page still asserts it; pages end up with no incoming
links; topics get referenced but never developed. Left alone, the connections
that give the vault its value ([[connection-maintenance]]) quietly go stale.

Linting is a scheduled walk of the whole wiki that reports these problems.
The cardinal rule is **report, don't delete** — the agent surfaces what needs
attention with file paths; the owner decides what changes. In this vault the
work is split:

- **Mechanical checks** are deterministic code, not model judgment:
  `scripts/vault_check.py` catches broken wikilinks, orphans, index drift,
  and missing frontmatter, and fails loudly (exit 1).
- **Semantic checks** need the agent: contradictions, supersession, and
  coverage gaps, run weekly as part of the [[second-brain-loop]].

Treat lint as a core operation, not an optional extra — it is what separates
a second brain that stays sharp from one that quietly becomes a mess.

## Links

- [[second-brain-loop]] — lint is the loop's maintenance phase
- [[connection-maintenance]] — lint backstops the connections that slip through
- [[compiled-knowledge-vs-rag]] — maintenance is the price of compiled knowledge
- [[schema-as-engine]] — report-don't-delete is encoded in the schema

## Source

- Guide: `raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf`
- Upstream: Andrej Karpathy, "LLM Knowledge Bases" —
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
