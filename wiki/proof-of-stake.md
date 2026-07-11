---
title: Proof of Stake
date: 2026-07-11
type: concept
source: https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/
tags: [crypto, foundations]
---

**Proof-of-stake replaces mining hardware with bonded capital: validators
lock coins as collateral, get randomly chosen to propose blocks, and are
financially destroyed ("slashed") if they cheat.**

Instead of burning energy, security comes from money at risk. A validator
(32 ETH on Ethereum) attests to blocks; provable misbehavior — signing two
conflicting blocks — triggers slashing of the stake. Attacking the chain
therefore requires acquiring and then vaporizing a huge fraction of the
asset itself. Ethereum's switch from [[proof-of-work]] to proof-of-stake
(the Merge, 15 September 2022) cut its energy use by ~99.95% and made ETH a
yield-bearing asset via staking rewards.

Trade-offs are real: capital compounds ("the rich stake more"), large
staking pools and liquid-staking protocols (Lido) concentrate validation,
and regulators have circled staking yield as a possible security-like
feature. Still, every major smart-contract chain launched since ~2020 —
Solana, Avalanche, and Ethereum post-Merge ([[layer-1-platforms]]) — uses
some form of stake-based consensus; [[bitcoin]] remains the notable
proof-of-work holdout.

## Links

- [[ethereum]] — the flagship proof-of-stake migration
- [[proof-of-work]] — the energy-based predecessor
- [[layer-1-platforms]] — the stake-secured competitor chains
- [[crypto]] — domain hub

## Source

- Ethereum docs, Proof-of-stake —
  https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/
- Ethereum, The Merge — https://ethereum.org/en/roadmap/merge/
