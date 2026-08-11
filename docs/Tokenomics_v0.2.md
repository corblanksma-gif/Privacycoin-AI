# Privacycoin AI – Tokenomics v0.2

**Status**: Working draft (uitgebreid)  
**Gerelateerde issue**: #2

## 1. Design Principles

- Privacy-first (fees en ownership moeten privacy-vriendelijk kunnen verlopen)
- Lage friction voor agents (micropayments moeten extreem goedkoop zijn)
- Duurzame incentives voor creators, compute-providers en validators
- Transparante financiering via 90% van de PRCY-premine
- Multi-chain ready (Solana execution + Aztec privacy + PRCY/PIVX)

## 2. Token

- **Ticker (voorstel)**: PCAI (of gemigreerde/upgraded PRCY)
- **Type**: Utility + Governance + Staking token
- **Multi-chain**: Native of wrapped op Solana, Aztec en eventueel andere lagen

## 3. Financiering via PRCY-premine

90% van de oorspronkelijke PRCY-premine (60 miljoen bij genesis) wordt ingezet.

### Voorgestelde allocatie

| Categorie                        | %    | Doel                                      | Vesting / Opmerkingen                  |
|----------------------------------|------|-------------------------------------------|----------------------------------------|
| Core Development & Research      | 35%  | zkML, agent protocol, bridges, audits     | 3–4 jaar linear + cliffs               |
| Liquidity & Market Making        | 20%  | Solana + Aztec liquiditeit                | Gedeeltelijk direct, rest gecontroleerd|
| Ecosystem Grants & Incentives    | 20%  | Builders, agents, compute, models         | Milestone-based                        |
| Treasury (lange termijn)         | 15%  | Multi-sig reserve                         | Strenge multi-sig + community vote     |
| Marketing & Community            | 10%  | Awareness, partnerships, events           | 2–3 jaar                               |

**Transparantie-eisen**:
- Multi-sig (minimaal 3/5 of 4/7)
- Publieke adressen
- Kwartaal on-chain + off-chain rapportages
- Grote uitgaven via governance vote

## 4. Utility van PCAI

1. **Staking**
   - Agent reputation staking (slashable)
   - Masternode / validator staking (waar van toepassing)
   - Compute provider staking

2. **Fees**
   - Marketplace fees (listing, success fee, royalty)
   - Agent-to-agent call fees
   - Privacy premium op Aztec (optioneel)

3. **Governance**
   - Protocol upgrades
   - Treasury besteding
   - Parameter changes (fees, slash percentages, etc.)

4. **Collateral**
   - Escrow collateral
   - Dispute resolution bonds

5. **Incentives**
   - Rewards voor valuable agents, high-quality models en reliable compute

## 5. Fee Model (voorstel)

- Solana layer: zeer lage fees (native Solana fees + kleine protocol fee)
- Aztec layer: iets hogere fee mogelijk voor privacy-garanties
- Royalty: creators ontvangen automatisch een percentage van usage
- Protocol treasury ontvangt een klein percentage van marketplace volume

## 6. Supply & Emissie (open punten)

- Exacte totale supply nog te bepalen
- Of er een migratie/upgrade van PRCY komt of een nieuwe token
- Eventuele burn-mechanismen (fees, slashing)
- Inflatie vs. fixed supply trade-off

## 7. Multi-chain Considerations

- Unified balance view voor gebruikers
- Bridge fees en security budget
- Liquidity incentives op beide primary chains (Solana + Aztec)

## 8. Risico’s

- Premine-perceptie → maximale transparantie en vesting
- Multi-chain liquidity fragmentatie
- Regulatory treatment van privacy + AI tokens

## 9. Volgende stappen

- [ ] Exacte supply en emissieschema vastleggen
- [ ] Vesting contracts specificeren
- [ ] Fee percentages modelleren
- [ ] Legal review van premine-allocatie
- [ ] Community feedback ronde

---
*Dit document vervangt de eerdere Tokenomics_Draft en wordt verder aangescherpt.*
