---
title: Blockchain
date: 2026-07-11
type: concept
source: https://bitcoin.org/bitcoin.pdf
tags: [crypto, foundations]
---

**A blockchain is an append-only ledger replicated across thousands of
computers that stays consistent without any central operator — because
rewriting its history is made economically prohibitive.**

Transactions are grouped into blocks; each block contains the cryptographic
hash of the previous one, so tampering with an old block invalidates every
block after it. A consensus mechanism — [[proof-of-work]] or
[[proof-of-stake]] — decides who appends the next block and makes attacking
the chain cost more than honest participation earns. The result is the one
thing databases never had: shared state that mutually distrusting parties
can rely on without a trusted middleman.

The honest engineering framing: a blockchain is a *terrible* database —
slow, expensive, replicated a thousandfold. It is only worth using when
removing the trusted operator is the whole point (money without banks
→ [[bitcoin]], contracts without courts → [[smart-contracts]]). When a
trusted operator is acceptable, a normal database beats it on every axis.

## Links

- [[bitcoin]] — the first and largest blockchain, built for money
- [[proof-of-work]] — the original mechanism securing the ledger
- [[proof-of-stake]] — the capital-based successor mechanism
- [[smart-contracts]] — programs deployed on blockchains
- [[crypto]] — domain hub

## Source

- Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System" (2008) —
  https://bitcoin.org/bitcoin.pdf
