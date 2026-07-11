---
title: Smart Contract Security
date: 2026-07-11
type: concept
source: https://owasp.org/www-project-smart-contract-top-10/
tags: [crypto, security]
---

**Smart contracts are immutable programs holding money in public — every
bug is a standing bounty claimable by anyone on Earth, which makes contract
auditing one of the highest-stakes security disciplines in software.**

The canonical vulnerability classes, each with famous corpses: *reentrancy*
(call out before updating state — [[the-dao-hack]]); *oracle manipulation*
(feed a contract a fake price via flash-loan-distorted pools, drain its
lending market); *access-control mistakes* (unprotected admin/initialize
functions — Poly Network, $611M); *upgradeable-proxy confusion*; *integer
and rounding errors*. Above the code sit the operational classes that now
dominate losses ([[crypto-hacks]]): compromised keys, malicious governance
proposals, and poisoned front-ends.

The defense stack that professionalized after 2020: multiple independent
audits (Trail of Bits, OpenZeppelin, Spearbit...), competitive audit
platforms (Code4rena, Sherlock), formal verification for core math, fuzzing
(Echidna/Foundry), on-chain monitoring with auto-pause, bug bounties to
$10M+ (Immunefi), and timelocked upgrades so users can exit before changes
apply. None of it is optional: [[defi]] TVL is a permanent red-team
engagement, and the sector's loss history *is* its audit syllabus.

## Links

- [[the-dao-hack]] — reentrancy, the founding lesson
- [[smart-contracts]] — why immutability raises the stakes
- [[crypto-hacks]] — the operational attacks beyond code
- [[defi]] — the value pool under permanent attack
- [[crypto]] — domain hub

## Source

- OWASP Smart Contract Top 10 —
  https://owasp.org/www-project-smart-contract-top-10/
