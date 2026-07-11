---
title: Connection Maintenance
date: 2026-07-11
type: concept
source: raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf
tags: [knowledge-systems]
---

**A vault's value lives in its connections, which grow quadratically while
notes grow linearly — so connection upkeep must be delegated to an agent or
the system collapses.**

With *n* notes there are n(n−1)/2 potential connections: 10 notes → 45,
100 → 4,950, 500 → ~125,000. No human re-checks their old notes against every
new source, so in manual systems the connections silently stop being made,
knowledge silos, and the vault dies — maintenance cost outgrows the
maintainer. This is the specific failure the agent removes: at ingest time it
searches the existing vault and wires the new [[atomic-notes]] in, both
directions, every time ([[second-brain-loop]]).

Practical limit worth remembering: "re-link against the *entire* vault" stops
being literal at scale. Past a few hundred pages the whole vault no longer
fits in one context window, so linking must be search-first — consult the
index, grep for candidates, read only those. The [[schema-as-engine]] here
mandates search-first from day one, and [[wiki-linting]] exists to catch the
connections that slip through anyway.

## Links

- [[second-brain-loop]] — ingest is where connections get made
- [[atomic-notes]] — precise connections require atomic endpoints
- [[wiki-linting]] — the backstop for missed or decayed connections
- [[schema-as-engine]] — encodes the search-first linking rule

## Source

- Guide: `raw/processed/2026-07-11-obsidian-second-brain-claude-code-guide.pdf`
- Upstream: Andrej Karpathy, "LLM Knowledge Bases" —
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
