def make_decision(
    issue_type,
    image_quality,
    duplicate
):

    if duplicate:
        return {
            "claim_status": "needs_review",
            "risk_flag": "duplicate_image"
        }

    if image_quality == "blurry":
        return {
            "claim_status": "not_enough_information",
            "risk_flag": "blurry_image"
        }

    return {
        "claim_status": "supported",
        "risk_flag": ""
    }