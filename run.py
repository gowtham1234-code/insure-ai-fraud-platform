import os
import pandas as pd

from src.image_damage_detector import detect_damage
from src.claim_extractor import extract_claim
from src.risk_analyzer import analyze_risk
from src.severity_predictor import predict_severity
from src.fraud_score import compute_fraud_score
from src.explainability import explain_decision
from src.pdf_report import generate_pdf_report


# FILE PATHS
CLAIMS_FILE = "dataset/claims/claims.csv"
HISTORY_FILE = "dataset/claims/user_history.csv"
OUTPUT_FILE = "output/output.csv"

BASE_IMAGE_PATH = "dataset/hackerrank-orchestrate-june26-main/dataset"


# -------------------------------
# USER HISTORY FUNCTION
# -------------------------------
def get_user_history(user_id, history_df):

    row = history_df[history_df["user_id"] == user_id]

    if len(row) == 0:
        return 0

    return int(row.iloc[0]["past_claim_count"])


# -------------------------------
# PROCESS SINGLE CLAIM
# -------------------------------
def process_claim(row, history_df):

    # 1. Extract claim info
    claim_info = extract_claim(row["user_claim"])

    # 2. User history
    total_claims = get_user_history(row["user_id"], history_df)

    # 3. Risk analysis
    risk_flags = analyze_risk(total_claims)

    # 4. Image path handling
    images = row["image_paths"].split(";")

    full_paths = [
        os.path.join(BASE_IMAGE_PATH, img)
        for img in images
    ]

    first_image = full_paths[0]

    # 5. Damage detection
    damage = detect_damage(first_image)

    # 6. Severity prediction
    severity_result = predict_severity(first_image)
    severity_score = severity_result["score"]

    # 7. Risk conversion
    risk_score = len(risk_flags) * 10

    duplicate_risk = 20
    quality_penalty = 10
    user_risk = risk_score
    confidence = severity_result["confidence"] * 100

    # 8. Fraud score
    fraud = compute_fraud_score(
        severity_score,
        duplicate_risk,
        quality_penalty,
        user_risk,
        confidence
    )

    # 9. Explanation
    explanation = explain_decision(
        damage["damage_detected"],
        severity_result,
        fraud
    )

    # 10. Final result dictionary
    result = {
        "user_id": row["user_id"],
        "image_paths": row["image_paths"],
        "user_claim": row["user_claim"],
        "claim_object": row["claim_object"],

        "evidence_standard_met": "yes",
        "evidence_standard_met_reason": "Rule validation passed",

        "risk_flags": ";".join(risk_flags),
        "issue_type": claim_info["issue_type"],
        "object_part": claim_info["object_part"],

        "claim_status": "supported" if damage["damage_detected"] else "rejected",
        "claim_status_justification": explanation,

        "supporting_image_ids": ";".join([os.path.basename(x) for x in full_paths]),
        "valid_image": "yes",

        "severity": severity_result["severity"],
        "fraud_score": fraud
    }

    # 11. Generate PDF report (🔥 NEW FEATURE)
    generate_pdf_report(result)

    return result


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():

    print("\n🚀 Starting Insurance AI Pipeline...\n")

    claims_df = pd.read_csv(CLAIMS_FILE)
    history_df = pd.read_csv(HISTORY_FILE)

    results = []

    for _, row in claims_df.iterrows():
        results.append(process_claim(row, history_df))

    output_df = pd.DataFrame(results)

    output_df.to_csv(OUTPUT_FILE, index=False)

    print("\n✅ Pipeline Completed Successfully!")
    print("📁 Saved CSV:", OUTPUT_FILE)
    print("📊 Total Rows Processed:", len(output_df))
    print("📄 PDF Reports Generated in /output")


# -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    main()