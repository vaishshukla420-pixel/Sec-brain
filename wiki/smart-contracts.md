---
title: Smart Contracts
date: 2026-07-11
type: concept
source: https://ethereum.org/en/smart-contracts/
tags: [crypto, foundations]
---

**A smart contract is a program on a blockchain that holds money and
executes exactly as written, with no operator able to stop, reverse, or
amend it — automation of agreement, with the bug risk to match.**

Deployed code becomes a permanent on-chain actor: it can custody funds,
enforce rules, and interact with other contracts. Two properties make this
powerful. *Trustlessness*: counterparties rely on code, not on each other or
courts. *Composability*: contracts call contracts, so protocols stack like
"money legos" — a lending pool plugs into a DEX plugs into a yield vault —
which is the entire architecture of [[defi]].

The same properties are its danger. Immutability means a bug is not a
patch-Tuesday problem but an open vault: value-bearing code gets exploited
the moment a flaw is found ([[smart-contract-security]]), a lesson learned
catastrophically in [[the-dao-hack]]. And contracts can only see on-chain
data — anything from the outside world (prices, weather, election results)
must be delivered by *oracles* (Chainlink et al.), which become their own
trust assumption and attack surface.

## Links

- [[ethereum]] — the platform that made contracts mainstream
- [[defi]] — the largest application of composable contracts
- [[the-dao-hack]] — the founding disaster of contract risk
- [[smart-contract-security]] — the audit discipline the risk created
- [[crypto]] — domain hub

## Source

- Ethereum docs, Smart contracts — https://ethereum.org/en/smart-contracts/
