def analyze_risk(total_claims):

    flags = []

    if total_claims > 10:
        flags.append("frequent_claims")

    if total_claims > 20:
        flags.append("high_claim_volume")

    return flags