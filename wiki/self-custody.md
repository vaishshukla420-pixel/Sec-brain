---
title: Self-Custody
date: 2026-07-11
type: concept
source: https://en.wikipedia.org/wiki/Cryptocurrency_wallet
tags: [crypto, foundations, security]
---

**Whoever holds the private key owns the coins — "not your keys, not your
coins" — and every major custodial collapse in crypto history is this rule
teaching itself the hard way.**

A wallet doesn't store coins; it stores the private key that authorizes
moving them on the [[blockchain]]. Hand that key (or the coins) to an
exchange and you own a *claim on a company*, not an asset — a distinction
customers of [[mt-gox-collapse]] (2014) and [[ftx-collapse]] (2022)
discovered in bankruptcy court. Self-custody options run from hot wallets
(software, convenient, phishable) to hardware wallets (keys never touch the
internet) to multisig/MPC setups for institutions.

The trade-off is unforgiving in both directions: custodians can lose your
coins for you, but self-custody means there is no password reset, no fraud
department, no undo — lose the seed phrase or sign one malicious
transaction ([[crypto-scams]] wallet drainers) and the money is simply
gone. Post-FTX, the pendulum swung visibly: hardware wallet sales spiked,
exchanges published proof-of-reserves, and regulated custody became an
institutional product ([[institutional-adoption]]).

## Links

- [[mt-gox-collapse]] — custody lesson #1 (2014)
- [[ftx-collapse]] — custody lesson #2, at 10x scale (2022)
- [[crypto-scams]] — the attacks self-custody exposes you to
- [[cefi-exchanges]] — the custodial alternative and its risks
- [[crypto]] — domain hub

## Source

- https://en.wikipedia.org/wiki/Cryptocurrency_wallet
