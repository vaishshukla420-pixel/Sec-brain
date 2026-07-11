---
title: Crypto Hacks
date: 2026-07-11
type: concept
source: https://en.wikipedia.org/wiki/2022_Ronin_Network_hack
tags: [crypto, security]
---

**Crypto suffers billion-dollar thefts routinely — bridges and exchange hot
wallets are the fattest targets, North Korea's Lazarus Group is the most
prolific attacker, and stolen funds move through a professionalized
laundering pipeline.**

The greatest hits: Ronin bridge, $625M (March 2022, Lazarus); Poly Network,
$611M (2021, returned); Wormhole, $326M (2022); and Bybit, ~$1.5B (February
2025) — the largest theft in crypto history, executed not by breaking
cryptography but by compromising the multisig signing UI so executives
approved a malicious transaction. That is the pattern to internalize:
modern mega-hacks target *operational* layers — key ceremonies, signer
devices, front-ends, social engineering — more than [[smart-contracts]]
themselves ([[smart-contract-security]] covers the code side).

Cross-chain bridges deserve their reputation as the worst attack surface:
they concentrate two chains' worth of value behind one contract or one
multisig ([[layer-2-scaling]] rollups partially exist to reduce this).
State-level context: UN and Chainalysis attribute multi-billion-dollar
cumulative takings to North Korea, funding its weapons program — which is
why exchange hacks are a sanctions issue, not just a security one
([[privacy-tech]] mixers sit in the middle of that fight). Chainalysis
counted ~$2.2B stolen in 2024; 2025 blew past that on Bybit alone.

## Links

- [[smart-contract-security]] — the code-level defense discipline
- [[cefi-exchanges]] — hot wallets, the perennial target
- [[privacy-tech]] — where stolen funds go to wash
- [[crypto-scams]] — retail-scale crime, same economy
- [[crypto]] — domain hub

## Source

- https://en.wikipedia.org/wiki/2022_Ronin_Network_hack
- Chainalysis Crypto Crime Reports — https://www.chainalysis.com/blog/
