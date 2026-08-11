# Privacycoin AI Chain – Project Structure (Scaffold)

Dit is een **scaffold** voor de eventuele nieuwe chain.  
Het is geen werkende blockchain, maar de mappenstructuur en documentatie om later serieus te kunnen bouwen.

## Aanbevolen technische richting

Zie `../docs/New_Chain_Design.md` voor het volledige ontwerp.

**Korte termijn realiteit**:  
Gebruik de hybride architectuur (Solana + Aztec + PRCY/PIVX).  
Een volledig nieuwe L1 is een meerjarenproject.

## Mappenstructuur (voorstel)

```
chain/
├── README.md                 # Dit bestand
├── docs/                     # Chain-specifieke documentatie
├── specs/                    # Formele specificaties
│   ├── consensus.md
│   ├── privacy.md
│   ├── agent_primitives.md
│   └── bridges.md
├── proto/                    # Protobuf / interface definities
├── node/                     # Node implementatie (later)
├── runtime/                  # Runtime / VM
├── privacy/                  # RingCT / ZK modules
├── agents/                   # Native agent primitives
├── bridges/                  # Bridge modules
├── scripts/                  # Genesis, keygen, etc.
└── tests/
```

## Volgende concrete stappen als we een eigen chain willen

1. Kies framework (Cosmos SDK / Substrate / eigen / zk-rollup stack)
2. Schrijf formele specs voor consensus + privacy model
3. Bouw minimale shielded transfer testnet
4. Voeg agent identity + escrow toe
5. Security audits voordat mainnet

## Huidige status

Alleen documentatie en scaffold. Geen productie-code.
