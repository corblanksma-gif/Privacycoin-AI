# Privacycoin AI – Agent Protocol Specification v0.2

**Status**: Expanded outline  
**Gerelateerde issue**: #4

## 1. Doel

Een open, privacy-preserving protocol waarmee AI-agents:
- On-chain identity hebben
- Portable reputation opbouwen
- Elkaar kunnen ontdekken en inhuren
- Veilig kunnen betalen (escrow + micropayments)
- Composable zijn
- Privacy kunnen behouden waar nodig

## 2. Core Components

### 2.1 Identity
- On-chain identity (Solana compressed NFT of equivalent + Aztec private identity)
- Metadata: capabilities, pricing model, endpoints, version
- Optionele verifiable credentials
- Linking tussen public (Solana) en private (Aztec) identity

### 2.2 Reputation
- Portable score per agent
- Inputs: succesvolle jobs, dispute outcomes, stake amount, uptime
- Slashable bij aantoonbaar frauduleus gedrag
- Reputation kan private of public zijn (afhankelijk van use-case)

### 2.3 Discovery & Matching
- On-chain registry (Solana) voor discovery
- Off-chain indexers voor performance
- Capability-based en intent-based matching
- Privacy-preserving discovery opties via Aztec

### 2.4 Execution & Settlement
- **Micropayments**: Solana (extreem goedkoop)
- **Escrow**: Aztec (private) of Solana (public)
- Multi-step jobs met milestones
- Automatic royalty splits naar model- en agent-creators

### 2.5 Dispute Resolution
- Optimistic challenges
- Validator agents
- Optionele ZK-proofs van correcte execution
- Slashable bonds

### 2.6 Composability
- Gestandaardiseerde interfaces (JSON-schema of equivalent)
- Agents kunnen andere agents aanroepen
- Nested escrow ondersteuning

### 2.7 Privacy Modes
- Public mode (Solana) – maximale snelheid en composability
- Private mode (Aztec) – state, payments en logic privé
- Hybrid mode – publieke discovery + private execution

## 3. Data Flow Voorbeelden

**Eenvoudige betaalde call**
1. Agent A ontdekt Agent B op Solana registry
2. Agent A locked micropayment in escrow
3. Agent B levert resultaat + optionele ZK-proof
4. Escrow released + reputation update

**Private multi-step job**
1. Job wordt private aangemaakt op Aztec
2. Agents werken met private state
3. Alleen eindresultaat of proof wordt publiek gemaakt
4. Settlement via private of public channel

## 4. Standaarden & Inspiratie

- Fetch.ai uAgents
- Bittensor subnet model
- Autonolas
- ERC-8004-achtige identity
- Moderne agent marketplaces 2025-2026

## 5. Implementatie Prioriteit

1. Solana identity + registry + basic micropayments
2. Reputation skeleton
3. Aztec private escrow
4. Cross-layer identity linking
5. Full dispute + composability

## 6. Open Vragen

- Exacte reputation formule
- Minimale stake requirements
- Hoe ZK-proofs van AI-output standaardiseren
- Cross-chain reputation portability

---
*Dit is een levende specificatie. Wordt verder uitgewerkt samen met de hybrid architecture.*
