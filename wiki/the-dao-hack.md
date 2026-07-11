---
title: The DAO Hack
date: 2026-07-11
type: concept
source: https://en.wikipedia.org/wiki/The_DAO
tags: [crypto, history, security]
---

**In June 2016 an attacker drained ~3.6M ETH from The DAO — the largest
crowdfund in history at the time — and Ethereum's response, rewriting the
ledger to undo it, permanently split both the chain and crypto's
philosophy.**

The DAO was a smart-contract venture fund holding ~$150M (about 14% of all
ETH). A *reentrancy* bug — the contract sent funds before updating its
balance, so a malicious contract could recursively re-enter and withdraw
repeatedly — let the attacker siphon roughly a third of it. The Ethereum
community faced a pure version of crypto's core question: is "code is law"
literal, or does social consensus outrank the ledger? By majority, it chose
a hard fork (20 July 2016) that returned the funds. The minority kept
mining the original chain as Ethereum Classic (ETC), where the theft
stands.

Consequences that still matter: reentrancy became the canonical
smart-contract vulnerability class taught in every audit
([[smart-contract-security]]); the fork proved big chains *can* be socially
rewritten under enough pressure — a precedent [[ethereum]] has pointedly
never used again; and the SEC's 2017 "DAO Report" was US regulators' first
formal claim that many tokens are securities ([[crypto-regulation]]).

## Links

- [[smart-contracts]] — the immutability double-edge, demonstrated
- [[smart-contract-security]] — the discipline this exploit founded
- [[ethereum-launch]] — one year in, the project's defining crisis
- [[crypto-regulation]] — the SEC's DAO Report started token securities law
- [[crypto]] — domain hub

## Source

- https://en.wikipedia.org/wiki/The_DAO
- Ethereum Foundation, hard fork announcement —
  https://blog.ethereum.org/2016/07/20/hard-fork-completed
