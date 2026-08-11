# Dependencies & Source Repositories

Privacycoin AI bouwt voort op bestaande privacy-technologie. Hieronder de officiële repositories die relevant zijn.

## Core Privacy Bases

### PRCY Coin
- **Repo**: https://github.com/PRCYCoin/PRCYCoin
- **Doel**: RingCT, Ring Signatures (27-32), Bulletproofs, Stealth Addresses, PoS + Masternodes + PoA
- **Clone (shallow)**:
```bash
git clone --depth 1 https://github.com/PRCYCoin/PRCYCoin.git
```

### PIVX
- **Repo**: https://github.com/PIVX-Project/PIVX
- **Doel**: SHIELD protocol (Sapling zk-SNARKs), view keys, shielded staking
- **Clone (shallow)**:
```bash
git clone --depth 1 https://github.com/PIVX-Project/PIVX.git
```

## Hybrid Architecture Related

### Solana
- **Repo**: https://github.com/solana-labs/solana (of anza-xyz/agave)
- **Doel**: Execution layer voor agents & marktplaats (snel + goedkoop)

### Aztec
- **Repo**: https://github.com/AztecProtocol/aztec-packages
- **Doel**: Programmeerbare privacy + private smart contracts (Noir)

### Andere nuttige referenties
- EZKL / zkML tools: zoek op GitHub naar actuele zkML compilers
- Agent frameworks: elizaOS, Fetch.ai uAgents, etc.

## Aanbevolen lokale setup

```bash
mkdir -p dependencies
cd dependencies
git clone --depth 1 https://github.com/PRCYCoin/PRCYCoin.git
git clone --depth 1 https://github.com/PIVX-Project/PIVX.git
# Optioneel:
# git clone --depth 1 https://github.com/AztecProtocol/aztec-packages.git
```

> **Let op**: De volledige Bitcoin-derived repositories (PRCY, PIVX) zijn groot. Gebruik altijd `--depth 1` tenzij je de volledige geschiedenis nodig hebt.

## Status in deze repository

Deze Privacycoin-AI repository bevat **geen** git-submodules van de bovenstaande projecten (vanwege grootte).  
Clone ze lokaal wanneer je due diligence of code-analyse wilt doen (zie issue #3).
