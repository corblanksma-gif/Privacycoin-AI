# Clone Status & Instructions

## Quick start (aanbevolen)

Voer dit lokaal uit:

```bash
bash scripts/clone_dependencies.sh
```

of handmatig:

```bash
mkdir -p dependencies && cd dependencies
git clone --depth 1 https://github.com/PRCYCoin/PRCYCoin.git
git clone --depth 1 https://github.com/PIVX-Project/PIVX.git
git clone --depth 1 https://github.com/anza-xyz/agave.git
git clone --depth 1 https://github.com/AztecProtocol/aztec-packages.git
```

## Repositories

| Project | URL | Rol in Privacycoin AI |
|---------|-----|-----------------------|
| PRCY Coin | https://github.com/PRCYCoin/PRCYCoin | Privacy base (RingCT, Bulletproofs) |
| PIVX | https://github.com/PIVX-Project/PIVX | Privacy base (SHIELD zk-SNARKs) |
| Agave | https://github.com/anza-xyz/agave | Solana execution layer |
| Aztec Packages | https://github.com/AztecProtocol/aztec-packages | Programmeerbare privacy layer |

## Opmerking

Deze repositories zijn groot. Gebruik altijd `--depth 1`.  
Ze worden **niet** als submodules in deze repo gezet vanwege omvang.
