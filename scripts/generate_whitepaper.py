#!/usr/bin/env python3
"""
Privacycoin AI - Full Whitepaper Generator
Professional multi-page PDF using reportlab Platypus

Install dependencies:
    pip install reportlab

Generate the PDF:
    python scripts/generate_whitepaper.py

This produces Privacycoin_AI_Whitepaper_v1.0.pdf with the complete whitepaper.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    HRFlowable
)
from datetime import datetime

PRIMARY = HexColor("#0A1628")
ACCENT = HexColor("#00D4AA")
DARK = HexColor("#1A2332")
LIGHT_GRAY = HexColor("#F5F7FA")
MED_GRAY = HexColor("#6B7280")
TABLE_HEADER = HexColor("#0F766E")

def create_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CoverTitle', fontName='Helvetica-Bold', fontSize=28, textColor=PRIMARY, alignment=TA_CENTER, spaceAfter=12, leading=34))
    styles.add(ParagraphStyle(name='CoverSubtitle', fontName='Helvetica', fontSize=14, textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=8, leading=18))
    styles.add(ParagraphStyle(name='SectionHeader', fontName='Helvetica-Bold', fontSize=16, textColor=PRIMARY, spaceBefore=20, spaceAfter=10, leading=20))
    styles.add(ParagraphStyle(name='SubHeader', fontName='Helvetica-Bold', fontSize=12, textColor=DARK, spaceBefore=14, spaceAfter=6, leading=15))
    styles.add(ParagraphStyle(name='BodyTextJustify', fontName='Helvetica', fontSize=10, textColor=black, alignment=TA_JUSTIFY, spaceBefore=4, spaceAfter=6, leading=14))
    styles.add(ParagraphStyle(name='BulletText', fontName='Helvetica', fontSize=10, textColor=black, alignment=TA_LEFT, spaceBefore=2, spaceAfter=2, leading=13, leftIndent=15))
    styles.add(ParagraphStyle(name='TableCell', fontName='Helvetica', fontSize=8, textColor=black, leading=11))
    styles.add(ParagraphStyle(name='TableHeader', fontName='Helvetica-Bold', fontSize=8, textColor=white, leading=11))
    styles.add(ParagraphStyle(name='Footer', fontName='Helvetica', fontSize=8, textColor=MED_GRAY, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='Disclaimer', fontName='Helvetica-Oblique', fontSize=8, textColor=MED_GRAY, alignment=TA_JUSTIFY, leading=11))
    styles.add(ParagraphStyle(name='Quote', fontName='Helvetica-Oblique', fontSize=11, textColor=DARK, alignment=TA_CENTER, spaceBefore=10, spaceAfter=10, leading=15))
    return styles

def add_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MED_GRAY)
    canvas.drawString(20*mm, 12*mm, "Privacycoin AI Whitepaper v1.0")
    canvas.drawRightString(A4[0] - 20*mm, 12*mm, f"Pagina {doc.page}")
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(0.5)
    canvas.line(20*mm, 16*mm, A4[0] - 20*mm, 16*mm)
    canvas.restoreState()

def build_whitepaper():
    output_path = "Privacycoin_AI_Whitepaper_v1.0.pdf"
    doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=22*mm, bottomMargin=22*mm)
    styles = create_styles()
    story = []

    # ========== COVER ==========
    story.append(Spacer(1, 40*mm))
    story.append(Paragraph("PRIVACYCOIN AI", styles['CoverTitle']))
    story.append(Spacer(1, 6*mm))
    story.append(HRFlowable(width="60%", thickness=2, color=ACCENT, spaceBefore=5, spaceAfter=5, hAlign='CENTER'))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Een gedecentraliseerd open AI-platform met marktplaats<br/>voor AI-apps en onderling gekoppelde AI-agents", styles['CoverSubtitle']))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Gebouwd op de privacy-technologie van PRCY Coin & PIVX SHIELD<br/>Gecombineerd met zero-knowledge proofs en best practices uit de decentralized AI-sector", styles['CoverSubtitle']))
    story.append(Spacer(1, 15*mm))
    story.append(Paragraph("<b>Whitepaper Versie 1.0</b>", styles['CoverSubtitle']))
    story.append(Paragraph("Augustus 2026", styles['CoverSubtitle']))
    story.append(Spacer(1, 20*mm))
    story.append(Paragraph("“Privacy is a right. Open AI should be too.”", styles['Quote']))
    story.append(PageBreak())

    # ========== 1. EXECUTIVE SUMMARY ==========
    story.append(Paragraph("1. Executive Summary", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("Privacycoin AI (PCAI) is een nieuw crypto-project dat de kracht van privacy-coins combineert met een volledig gedecentraliseerd open AI-ecosysteem. Het platform biedt een marktplaats waar developers AI-apps, models en autonome agents kunnen publiceren, verkopen of verhuren. Agents kunnen onderling koppelen, taken uitvoeren, betalen en reputatie opbouwen — alles met sterke privacy-garanties.", styles['BodyTextJustify']))
    story.append(Paragraph("Het project hergebruikt en versterkt de bestaande technologie van <b>PRCY Coin</b> (RingCT, Ring Signatures 27-32, Bulletproofs, Stealth Addresses, PoS + Masternodes + Proof-of-Audit) en <b>PIVX</b> (SHIELD-protocol op basis van zk-SNARKs Sapling). Hierop wordt een moderne zkML-laag toegevoegd voor verifieerbare AI-inference zonder model- of data-lekken.", styles['BodyTextJustify']))
    story.append(Paragraph("<b>Financiering:</b> 90% van de oorspronkelijke PRCY-premine (60 miljoen PRCY bij genesis) wordt gericht ingezet voor development, liquiditeit, ecosystem grants, treasury en marketing van Privacycoin AI via multi-sig wallets met vesting en publieke rapportage.", styles['BodyTextJustify']))

    # ========== 2. VISIE ==========
    story.append(Paragraph("2. Visie & Probleemstelling", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("2.1 Het probleem", styles['SubHeader']))
    story.append(Paragraph("Huidige AI-systemen zijn grotendeels gecentraliseerd. Een handvol bedrijven controleren de beste modellen, de trainingsdata en de infrastructuur. Gebruikers hebben geen ownership over de AI die ze gebruiken en hun data wordt systematisch verzameld. Privacy-coins en decentralized AI-projecten zijn nog te gefragmenteerd om een volledig alternatief te bieden.", styles['BodyTextJustify']))
    story.append(Paragraph("2.2 De oplossing", styles['SubHeader']))
    story.append(Paragraph("Privacycoin AI levert een geïntegreerd platform waarin AI-models en agents als on-chain assets bestaan, met sterke transactionele en computationele privacy via RingCT + zk-SNARKs + zkML, een open marktplaats, agent-to-agent economie met escrow en reputatie, en een hybride architectuur (compute off-chain, settlement on-chain).", styles['BodyTextJustify']))

    # ========== 3. TECHNISCHE ARCHITECTUUR ==========
    story.append(Paragraph("3. Technische Architectuur", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("3.1 Privacy Base Layer", styles['SubHeader']))
    story.append(Paragraph("<b>PRCY Coin:</b> Ring Confidential Transactions (RingCT), Ring Signatures met dynamische ringgrootte 27-32, Bulletproofs (geen trusted setup), verplichte stealth addresses, Proof-of-Stake v3, Masternodes (5.000 PRCY collateral) en Proof-of-Audit (PoA).", styles['BodyTextJustify']))
    story.append(Paragraph("<b>PIVX SHIELD:</b> Custom implementatie van het Sapling-protocol met zk-SNARKs (Groth16). Lichte proofs, snelle generatie/verificatie, view-keys voor selectieve disclosure en ondersteuning voor shielded staking.", styles['BodyTextJustify']))
    story.append(Paragraph("3.2 Zero-Knowledge Machine Learning (zkML)", styles['SubHeader']))
    story.append(Paragraph("Voor verifieerbare AI-inference wordt een moderne zkML-stack gebruikt (operator-level decomposition, recursieve proofs, quantisatie-vriendelijke circuits), gebaseerd op best practices uit EZKL, DeepProve en OpenLLM. Een agent kan bewijzen dat een output correct is berekend zonder modelgewichten of private input te onthullen.", styles['BodyTextJustify']))
    story.append(Paragraph("3.3 Smart Contracts & Agents", styles['SubHeader']))
    story.append(Paragraph("Omdat native PRCY en PIVX geen volledige EVM bieden, wordt een EVM-compatibele sidechain of L2 gebruikt met privacy-bridges. Agents krijgen on-chain identity (NFT-achtig), portable reputation, discovery, escrow, micropayments en composability (agents die andere agents aanroepen).", styles['BodyTextJustify']))

    # ========== 4. UITDAGINGEN ==========
    story.append(Paragraph("4. Uitdagingen & Belemmeringen", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    header = [Paragraph("<b>Categorie</b>", styles['TableHeader']), Paragraph("<b>Uitdaging</b>", styles['TableHeader']), Paragraph("<b>Ernst</b>", styles['TableHeader']), Paragraph("<b>Mitigatie</b>", styles['TableHeader'])]
    data = [header]
    challenges = [
        ("Schaalbaarheid", "RingCT + zkML rekenintensief", "Hoog", "Hybride + batching + L2"),
        ("Verifieerbaarheid AI", "Bewijs correcte inference zonder lekken", "Zeer hoog", "zkML + optioneel TEE"),
        ("Smart contracts", "Geen native EVM op PRCY/PIVX", "Hoog", "Sidechain / bridges"),
        ("Compute", "AI-inference duur", "Hoog", "Decentrale GPU-netwerken"),
        ("Regulering", "Privacy-coins delisting-risico", "Hoog", "View-keys + selective disclosure"),
        ("Liquiditeit", "Kleine marketcap PRCY", "Hoog", "90% premine voor liquiditeit"),
    ]
    for cat, uit, ernst, mit in challenges:
        data.append([Paragraph(cat, styles['TableCell']), Paragraph(uit, styles['TableCell']), Paragraph(ernst, styles['TableCell']), Paragraph(mit, styles['TableCell'])])
    t = Table(data, colWidths=[32*mm, 55*mm, 22*mm, 55*mm], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('GRID', (0, 0), (-1, -1), 0.4, MED_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_GRAY]),
    ]))
    story.append(t)
    story.append(Spacer(1, 4*mm))

    # ========== 5. TOKENOMICS ==========
    story.append(Paragraph("5. Tokenomics", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("90% van de PRCY-premine wordt via multi-sig + vesting + publieke rapportage ingezet. Voorgestelde verdeling: 35% Core Development & Research, 20% Liquidity, 20% Ecosystem Grants, 15% Treasury, 10% Marketing. Utility omvat staking, marketplace-fees, governance, reputation-staking en collateral.", styles['BodyTextJustify']))

    # ========== 6. ROADMAP ==========
    story.append(Paragraph("6. Roadmap", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("<b>Fase 0 (Q3–Q4 2026)</b>: Foundation, multi-sig treasury, due diligence<br/><b>Fase 1 (Q1–Q2 2027)</b>: Privacy-core + bridges + basis contracts<br/><b>Fase 2 (Q3–Q4 2027)</b>: zkML-pipelines + agent-framework testnet<br/><b>Fase 3 (2028)</b>: Mainnet marktplaats + governance<br/><b>Fase 4 (2029+)</b>: Schaal, cross-chain agents, post-quantum traject", styles['BodyTextJustify']))

    # ========== 7. GOVERNANCE ==========
    story.append(Paragraph("7. Governance & Transparantie", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("On-chain governance via masternodes + token-holders. Open-source repositories. Onafhankelijke audits van smart contracts en zk-circuits. Kwartaalrapportages over premine-uitgaven.", styles['BodyTextJustify']))

    # ========== 8. CONCLUSIE ==========
    story.append(Paragraph("8. Conclusie", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("Privacycoin AI is technisch haalbaar door de sterke privacy-basissen van PRCY en PIVX te combineren met zkML en agent-economies. Door 90% van de PRCY-premine gericht in te zetten, krijgt het project de middelen om een echt open, privacy-first AI-ecosysteem te bouwen.", styles['BodyTextJustify']))
    story.append(Paragraph("Privacy is a right. Open AI should be too.", styles['Quote']))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Dit is een concept-whitepaper. Alle technische specificaties, exacte tokenomics en de definitieve premine-allocatie worden verder uitgewerkt na community-feedback en technische audits.", styles['Disclaimer']))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("— Einde Whitepaper —", styles['CoverSubtitle']))
    story.append(Paragraph(f"Gegenereerd op {datetime.now().strftime('%d %B %Y')}", styles['Footer']))

    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Whitepaper generated: {output_path}")
    return output_path

if __name__ == "__main__":
    build_whitepaper()
