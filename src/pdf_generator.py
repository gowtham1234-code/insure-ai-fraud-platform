import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_claim_pdf(damage, severity, fraud_score, explanation, filename="output/claim_report.pdf"):
    """
    Compiles data points directly into an enterprise-style PDF artifact.
    Branded under Lead Architect: Gowtham
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()
    
    # Designer Color Palette
    navy_primary = colors.HexColor("#1A365D")
    neutral_dark = colors.HexColor("#2D3748")
    
    # Document Header Title
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontSize=22, textColor=navy_primary, spaceAfter=4)
    story.append(Paragraph("🛡️ InsureAI Verification & Audit Document", title_style))
    
    # Metadata Branding Row
    meta_style = ParagraphStyle('DocMeta', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor("#718096"))
    story.append(Paragraph("<b>Platform System Architect:</b> Gowtham &nbsp;&bull;&nbsp; <b>Classification Tier:</b> Live Forensic Analysis", meta_style))
    story.append(Spacer(1, 15))
    
    # Core Data Metrics Grid Block
    grid_data = [
        [Paragraph("<b>Evaluation Vector</b>", styles['Normal']), Paragraph("<b>System Metric Output</b>", styles['Normal'])],
        ["Computer Vision Structural Assessment", damage.get('damage_type', 'N/A')],
        ["Impact Severity Classification", severity.get('severity', 'N/A')],
        ["Consolidated Fraud Probability Indicator", f"{fraud_score}/100"]
    ]
    
    metrics_table = Table(grid_data, colWidths=[200, 320])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('TEXTCOLOR', (0,0), (-1,0), navy_primary),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(metrics_table)
    story.append(Spacer(1, 20))
    
    # Forensic AI Text block section
    story.append(Paragraph("<b>🧠 XAI Automated Audit Summary Narrative:</b>", ParagraphStyle('Sub', parent=styles['Heading2'], fontSize=12, textColor=navy_primary, spaceAfter=8)))
    
    clean_explanation = explanation.replace('\n', '<br/>')
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontSize=10, textColor=neutral_dark, leading=14)
    story.append(Paragraph(clean_explanation, body_style))
    
    doc.build(story)
    return filename