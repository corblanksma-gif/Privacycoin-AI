# Agent Protocol Outline (v0.1)

> Status: Outline / work in progress  
> Gerelateerde issue: #4

## 1. Doel

Een open, privacy-preserving protocol waarmee AI-agents:
- zich on-chain kunnen identificeren
- reputatie opbouwen
- elkaar kunnen ontdekken en inhuren
- veilig betalen (escrow / micropayments)
- composable zijn (agents die andere agents aanroepen)

## 2. Core componenten

### 2.1 Identity
- On-chain identity (NFT of equivalent)
- Metadata: capabilities, pricing, endpoints
- Optioneel: linked verifiable credentials

### 2.2 Reputation
- Portable across the marketplace
- Updates op basis van succesvolle jobs, disputes, staking
- Slashable bij frauduleus gedrag

### 2.3 Discovery & Matching
- On-chain registry + off-chain indexers
- Intent-based of capability-based matching

### 2.4 Execution & Settlement
- Escrow-contracten voor multi-step jobs
- Micropayments / pay-per-call voor gestandaardiseerde services
- Dispute resolution (validator-agents of optimistic + ZK)

### 2.5 Privacy
- Shielded payments waar mogelijk
- Selective disclosure via view-keys
- Geen onnodige leakage van agent-gedrag of data

### 2.6 Composability
- Agents kunnen andere agents aanroepen
- Gestandaardiseerde interfaces / schemas

## 3. Referenties / inspiratie

- Fetch.ai uAgents
- Bittensor subnets
- Autonolas
- ERC-8004-achtige identity standaarden
- Recente agent marketplaces (2025-2026)

## 4. Volgende stappen

- [ ] Concrete interface definities
- [ ] Smart contract skeletons
- [ ] Privacy threat model
- [ ] Testnet prototype

---
*Outline wordt verder uitgewerkt in issue #4.*
