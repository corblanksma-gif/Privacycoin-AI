# Dependencies & Source Repositories

Privacycoin AI bouwt voort op bestaande privacy- en high-performance technologie.

## Core Privacy Bases

### PRCY Coin
- **Repo**: https://github.com/PRCYCoin/PRCYCoin
- **Doel**: RingCT, Ring Signatures, Bulletproofs, Stealth Addresses, PoS + Masternodes
```bash
git clone --depth 1 https://github.com/PRCYCoin/PRCYCoin.git
```

### PIVX
- **Repo**: https://github.com/PIVX-Project/PIVX
- **Doel**: SHIELD (Sapling zk-SNARKs), view keys
```bash
git clone --depth 1 https://github.com/PIVX-Project/PIVX.git
```

## Hybrid Architecture – Execution & Privacy Layers

### Solana (Agave)
- **Repo**: https://github.com/anza-xyz/agave (huidige Solana validator / client)
- **Doel**: Execution layer voor agents, marktplaats en micropayments
```bash
git clone --depth 1 https://github.com/anza-xyz/agave.git
```

### Aztec
- **Repo**: https://github.com/AztecProtocol/aztec-packages
- **Doel**: Programmeerbare privacy, private smart contracts (Noir), private state
```bash
git clone --depth 1 https://github.com/AztecProtocol/aztec-packages.git
```

## Aanbevolen lokale setup (alles)

```bash
mkdir -p dependencies
cd dependencies

git clone --depth 1 https://github.com/PRCYCoin/PRCYCoin.git
git clone --depth 1 https://github.com/PIVX-Project/PIVX.git
git clone --depth 1 https://github.com/anza-xyz/agave.git
git clone --depth 1 https://github.com/AztecProtocol/aztec-packages.git
```

> **Belangrijk**: Deze repositories zijn groot. Gebruik altijd `--depth 1`. Volledige clones kunnen meerdere GB zijn.

## Status

Deze Privacycoin-AI repository bevat **geen** git-submodules van de bovenstaande projecten vanwege hun omvang. Clone ze lokaal voor code-analyse of due diligence.
