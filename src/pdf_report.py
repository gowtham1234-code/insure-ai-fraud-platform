from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf_report(data, filename="output/insurance_report.pdf"):
    """
    Generates a professional insurance claim report PDF
    """

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph("INSURANCE CLAIM AI REPORT", styles["Title"]))
    content.append(Spacer(1, 12))

    # Timestamp
    content.append(Paragraph(f"Generated On: {datetime.now()}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # User Info
    content.append(Paragraph(f"User ID: {data.get('user_id', 'N/A')}", styles["Normal"]))
    content.append(Spacer(1, 8))

    # Claim Info
    content.append(Paragraph(f"Claim Status: {data.get('claim_status', 'N/A')}", styles["Normal"]))
    content.append(Paragraph(f"Severity: {data.get('severity', 'N/A')}", styles["Normal"]))
    content.append(Paragraph(f"Fraud Score: {data.get('fraud_score', 'N/A')}", styles["Normal"]))
    content.append(Spacer(1, 8))

    # Risk
    content.append(Paragraph(f"Risk Flags: {data.get('risk_flags', 'None')}", styles["Normal"]))
    content.append(Spacer(1, 8))

    # Explanation
    content.append(Paragraph("AI Explanation:", styles["Heading2"]))
    content.append(Paragraph(data.get("claim_status_justification", ""), styles["Normal"]))

    doc.build(content)

    return filename