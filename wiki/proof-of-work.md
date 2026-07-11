---
title: Proof of Work
date: 2026-07-11
type: concept
source: https://bitcoin.org/bitcoin.pdf
tags: [crypto, foundations]
---

**Proof-of-work secures a blockchain by making block production cost real
energy: miners race to find a hash below a target, so rewriting history
means out-spending the entire honest network.**

Miners bundle transactions and brute-force a nonce until the block's hash
meets the difficulty target — a lottery where tickets are bought with
electricity. The winner earns newly issued coins (the block subsidy, cut in
half every four years — see [[bitcoin]]) plus fees. Difficulty re-adjusts
every 2,016 blocks (~2 weeks) so blocks keep arriving roughly every 10
minutes no matter how much hardware joins.

Security intuition: an attacker needs a majority of global hashpower (a
"51% attack") to rewrite recent history, and even then can only re-spend
their own coins, not steal others'. The energy expenditure — often criticized
as waste — *is* the security budget: it anchors the ledger to physical-world
cost. The open long-term question is what funds that budget as the subsidy
trends to zero and fees must carry it alone.

## Links

- [[blockchain]] — the structure proof-of-work secures
- [[bitcoin]] — the dominant proof-of-work network
- [[proof-of-stake]] — the alternative that replaces energy with bonded capital
- [[pre-bitcoin-digital-cash]] — Hashcash, where the idea came from
- [[crypto]] — domain hub

## Source

- Satoshi Nakamoto, Bitcoin whitepaper (2008) — https://bitcoin.org/bitcoin.pdf
- Adam Back, Hashcash (1997) — http://www.hashcash.org/
