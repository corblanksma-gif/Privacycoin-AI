#!/usr/bin/env python3
"""
Privacycoin AI - Full Whitepaper Generator
Professional multi-page PDF using reportlab Platypus

Install: pip install reportlab
Run: python generate_whitepaper.py
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

    # COVER
    story.append(Spacer(1, 40*mm))
    story.append(Paragraph("PRIVACYCOIN AI", styles['CoverTitle']))
    story.append(Spacer(1, 6*mm))
    story.append(HRFlowable(width="60%", thickness=2, color=ACCENT, spaceBefore=5, spaceAfter=5, hAlign='CENTER'))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Een gedecentraliseerd open AI-platform met marktplaats<br/>voor AI-apps en onderling gekoppelde AI-agents", styles['CoverSubtitle']))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Gebouwd op de privacy-technologie van PRCY Coin &amp; PIVX SHIELD<br/>Gecombineerd met zero-knowledge proofs en best practices uit de decentralized AI-sector", styles['CoverSubtitle']))
    story.append(Spacer(1, 15*mm))
    story.append(Paragraph("<b>Whitepaper Versie 1.0</b>", styles['CoverSubtitle']))
    story.append(Paragraph("Augustus 2026", styles['CoverSubtitle']))
    story.append(Spacer(1, 20*mm))
    story.append(Paragraph("“Privacy is a right. Open AI should be too.”", styles['Quote']))
    story.append(PageBreak())

    # Note: Full content is in the original generated PDF. This script is a simplified starter.
    # For the complete multi-section whitepaper, refer to the original generator used in the project.
    story.append(Paragraph("1. Executive Summary", styles['SectionHeader']))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    story.append(Paragraph("Privacycoin AI (PCAI) is een nieuw crypto-project dat de kracht van privacy-coins combineert met een volledig gedecentraliseerd open AI-ecosysteem. Zie de volledige whitepaper voor alle details over architectuur, agent-protocol, tokenomics (90% PRCY-premine), uitdagingen en roadmap.", styles['BodyTextJustify']))
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("— Einde samenvatting —", styles['CoverSubtitle']))
    story.append(Paragraph(f"Gegenereerd op {datetime.now().strftime('%d %B %Y')}", styles['Footer']))

    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Whitepaper generated: {output_path}")
    return output_path

if __name__ == "__main__":
    build_whitepaper()
