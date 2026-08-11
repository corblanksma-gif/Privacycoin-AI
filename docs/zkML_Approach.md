# zkML Approach for Privacycoin AI

**Status**: Initial approach document  
**Gerelateerde issue**: #5

## 1. Doel

Verifiable AI inference mogelijk maken zonder modelgewichten of private inputs te onthullen. Agents moeten kunnen bewijzen dat een bepaalde output correct is berekend.

## 2. Gekozen richting

**Hybride zkML**:
- Operator-level decomposition (circuits per primitive: matmul, softmax, activations, etc.)
- Recursieve / compositionele proofs
- Quantisatie-vriendelijke circuits om proving cost te verlagen
- Off-chain proving + on-chain verificatie (Solana of Aztec)

## 3. Relevante technologieën (2026)

- EZKL en vergelijkbare ONNX → circuit compilers
- DeepProve-achtige end-to-end LLM proving technieken
- OpenLLM / modulaire zkSNARK approaches
- Combinatie met TEE waar pure ZK te duur is

## 4. Architectuur

1. Model wordt geëxporteerd (ONNX of equivalent)
2. Relevante operators worden naar circuits vertaald
3. Prover (agent of dedicated prover network) genereert proof
4. Verifier smart contract (Solana of Aztec) checkt de proof
5. Alleen de proof + publieke inputs/outputs gaan on-chain

## 5. Privacy Modes

- Public verification (Solana) – goedkoop, snel
- Private verification (Aztec) – proof zelf ook privacy-vriendelijk
- Hybrid: public claim + private details

## 6. Kosten & Performance Overwegingen

- Full LLM end-to-end proving is in 2026 nog duur
- Focus eerst op kleinere models / specifieke operators / quantized models
- Progressive enhancement: start met optimistic + challenge, upgrade naar full ZK

## 7. Integratie met Agent Protocol

- Agent kan een “verifiable inference” capability adverteren
- Job kan eisen dat resultaat vergezeld gaat van ZK-proof
- Reputation kan hoger zijn voor agents die consistent correcte proofs leveren

## 8. Roadmap zkML

- Fase 1: Operator-level circuits + eenvoudige models
- Fase 2: Composition + betere quantisatie
- Fase 3: Integratie in agent jobs + marketplace
- Fase 4: Ondersteuning voor grotere models + prover market

---
*Dit is een startpunt. Wordt concreter naarmate prototypes ontstaan.*
