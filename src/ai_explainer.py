import os
from google import genai
from google.genai import types

def generate_ai_explanation(damage, severity, fraud_score):
    """
    Generates an expert forensic claims analysis using the live Gemini API.
    Developed by Gowtham.
    """
    # Initialize client (picks up GEMINI_API_KEY environment variable automatically)
    try:
        client = genai.Client()
    except Exception:
        return "⚠️ Gemini Environment Configuration Alert: Please ensure GEMINI_API_KEY is declared in your terminal env."

    prompt = f"""
    You are an elite AI insurance claim forensic analyst auditing a system platform built by lead developer Gowtham.
    Analyze this incoming vehicle claim data payload:
    
    - Detected Damage Type: {damage.get('damage_type', 'Unknown')} (Model Confidence: {damage.get('confidence', 0)*100:.1f}%)
    - Severity Classification: {severity.get('severity', 'Unknown')} (Numeric Intensity Score: {severity.get('score', 0)}/100)
    - Consolidated Fraud System Score: {fraud_score}/100
    
    Provide a professional, concise 3-line executive summary layout:
    1. Assess if the visual damage severity matches typical profiles for this damage type.
    2. Explain the forensic reasoning behind why the fraud risk metric calculated this specific score.
    3. Issue a definitive adjudication directive (Approve, Flag for Human Adjuster, or Fraud-Denial).
    Keep it corporate, direct, and elite. Do not mention system variables or JSON formatting structures.
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Live AI generation offline. Error tracing details: {str(e)}"