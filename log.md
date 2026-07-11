# Log

Append-only history of vault operations, newest at the bottom. Never rewritten.

## 2026-07-11

- **init** — Vault scaffolded: `raw/` inbox, `wiki/`, `index.md`, `log.md`,
  `CLAUDE.md` schema, `scripts/vault_check.py` (mechanical lint),
  `scripts/ingest.sh` (lockable headless sweep for cron).
- **ingest** — `2026-07-11-obsidian-second-brain-claude-code-guide.pdf`
  (20-page guide by @kirillk_web3 distilling Andrej Karpathy's
  LLM-knowledge-base gist; a cleaned text companion `.md` sits alongside the
  PDF): 6 pages added — [[second-brain-loop]] ★, [[atomic-notes]],
  [[compiled-knowledge-vs-rag]], [[connection-maintenance]],
  [[schema-as-engine]], [[wiki-linting]]; 0 updated. Excluded as
  non-knowledge content: the source's promotional sections (VPS affiliate
  pitch, Kimi K2.7 pitch, author's social links). Not carried into the wiki:
  the source's claim that Karpathy is "an Anthropic AI researcher" (false)
  and the unqualified claim that the agent "re-links against the entire
  vault" (holds only at small scale — see [[connection-maintenance]] for the
  search-first correction).
- **ingest** — Owner-directed bulk web-research ingest: "crypto A-to-Z"
  (explicit owner request, so the weekly GAP-FILL single-topic limit does
  not apply). 39 pages added under new domain hub [[crypto]] ★:
  foundations (10) — [[blockchain]], [[proof-of-work]], [[proof-of-stake]],
  [[bitcoin]] ★, [[ethereum]] ★, [[smart-contracts]], [[stablecoins]],
  [[tokenomics]], [[self-custody]], [[crypto-market-cycles]];
  history (11) — [[pre-bitcoin-digital-cash]], [[bitcoin-genesis]],
  [[mt-gox-collapse]], [[ethereum-launch]], [[the-dao-hack]], [[ico-boom]],
  [[defi-summer]], [[nft-mania]], [[terra-luna-collapse]], [[ftx-collapse]],
  [[bitcoin-spot-etf]]; sectors (9) — [[defi]] ★, [[cefi-exchanges]],
  [[layer-1-platforms]], [[layer-2-scaling]], [[nfts]], [[memecoins]],
  [[rwa-tokenization]], [[crypto-ai-intersection]], [[privacy-tech]];
  security (3) — [[crypto-hacks]], [[smart-contract-security]],
  [[crypto-scams]]; present & future (6) — [[crypto-2026-state]],
  [[crypto-regulation]], [[institutional-adoption]], [[cbdc]],
  [[bitcoin-digital-gold-thesis]], plus the [[crypto]] hub itself.
  Method: historical/conceptual pages compiled from stable knowledge with
  primary-source citations; the three synthesis pages
  ([[crypto-2026-state]], [[crypto-regulation]],
  [[institutional-adoption]]) built from three parallel web-research
  passes (~120 sources; API data from CoinGecko/DeFiLlama/L2Beat/rwa.xyz
  dated 2026-07-11; each page cites its verified URLs). Volatile market
  numbers deliberately centralized in [[crypto-2026-state]] (dated
  snapshot, supersede-don't-rewrite) so evergreen pages stay evergreen.
  Facts researched but held back as UNVERIFIED (single-source): Wisconsin
  pension exit date; Texas TRS $400M allocation; Render revenue figures;
  US Marshals seizure-wallet theft report. Web content treated as
  untrusted input per schema.
