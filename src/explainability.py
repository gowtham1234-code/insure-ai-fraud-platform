# src/explainability.py

def explain_decision(damage_detected, severity, fraud_score):

    if fraud_score > 70:
        risk_level = "HIGH RISK CLAIM"
    elif fraud_score > 40:
        risk_level = "MEDIUM RISK CLAIM"
    else:
        risk_level = "LOW RISK CLAIM"

    severity_level = severity["severity"]

    return (
        f"Damage detected: {damage_detected}. "
        f"Severity level: {severity_level}. "
        f"Fraud score indicates {risk_level}. "
        f"Model decision is based on image damage + risk signals."
    )