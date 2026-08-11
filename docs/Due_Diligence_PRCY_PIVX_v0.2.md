# Due Diligence – PRCY Coin & PIVX (v0.2)

**Status**: Expanded checklist + initial findings framework  
**Gerelateerde issue**: #3

## 1. Doel

Beoordelen in hoeverre de bestaande PRCY- en PIVX-codebases en ecosystemen geschikt zijn als privacy-fundament voor Privacycoin AI, en welke onderdelen hergebruikt, gebridged of vervangen moeten worden.

## 2. PRCY Coin

**Bronnen**: https://github.com/PRCYCoin/PRCYCoin , prcycoin.com

### Sterke punten
- RingCT + Ring Signatures (27-32)
- Bulletproofs (geen trusted setup)
- Verplichte stealth addresses
- PoS v3 + Masternodes (5.000 PRCY) + Proof-of-Audit
- Bestaande premine die als financieringsbron kan dienen

### Aandachtspunten
- Beperkte smart-contract capaciteit (geen volledige EVM)
- Relatief lage liquiditeit en marketcap (2026)
- Onderhoudsactiviteit en community-grootte
- Bridging-mogelijkheden naar moderne chains

### Te onderzoeken
- [ ] Exacte huidige codebase status en laatste meaningful commits
- [ ] Security history en eventuele audits
- [ ] Multi-sig / treasury status van de premine
- [ ] Wallet en explorer kwaliteit
- [ ] Mogelijkheid tot light-client of ZK-bridge

## 3. PIVX

**Bronnen**: https://github.com/PIVX-Project/PIVX , pivx.org

### Sterke punten
- SHIELD (Sapling zk-SNARKs) – een van de weinige productie zk-SNARK privacy-systemen op pure PoS
- View keys (selective disclosure)
- Masternodes + governance
- Langere track record dan PRCY

### Aandachtspunten
- Geen native EVM
- Shielded staking en volledige feature-set status in 2026
- Bridging en interoperabiliteit

### Te onderzoeken
- [ ] Huidige SHIELD implementatie en performance
- [ ] Maintenance en developer activity
- [ ] Governance effectiviteit
- [ ] Mogelijkheid tot hergebruik van SHIELD-componenten of bridge

## 4. Integratie-opties voor Privacycoin AI

| Optie | Beschrijving | Voordeel | Nadeel |
|-------|--------------|----------|--------|
| A. Pure bridge | PRCY/PIVX blijven aparte privacy-payment layers | Behoud bestaande privacy | Liquiditeit fragmentatie |
| B. Technology port | RingCT / SHIELD concepten hergebruiken in nieuwe stack | Moderne performance | Hoge development cost |
| C. Hybrid (aanbevolen) | PRCY/PIVX als max-privacy rail naast Solana + Aztec | Beste van beide werelden | Complexiteit |

## 5. Aanbeveling

**Hybride aanpak** (in lijn met Architecture_Hybrid_Recommendation.md):
- Houd PRCY + PIVX in leven als maximale privacy payment layer
- Bouw de agent marketplace en execution op Solana
- Gebruik Aztec voor programmeerbare privacy
- Investeer in veilige bridges

## 6. Volgende concrete stappen

- [ ] Code review van de belangrijkste privacy-modules
- [ ] Contact met huidige maintainers (indien actief)
- [ ] Bridge feasibility study
- [ ] Premine legal & technical status bevestigen

---
*Dit document wordt bijgewerkt naarmate de due diligence vordert.*
