# src/fraud_score.py

def compute_fraud_score(severity_score, duplicate_risk, quality_penalty, user_risk, confidence):
    """
    Combines multiple signals into a final fraud score (0–100)
    """

    score = (
        severity_score * 0.4 +
        duplicate_risk * 0.15 +
        quality_penalty * 0.15 +
        user_risk * 0.2 +
        confidence * 0.1
    )

    # clamp between 0 and 100
    score = max(0, min(100, score))

    return round(score, 2)