def extract_claim(conversation):

    text = conversation.lower()

    issue_type = "unknown"
    object_part = "unknown"

    damage_keywords = {
        "scratch": "scratch",
        "dent": "dent",
        "crack": "crack",
        "broken": "broken",
        "water": "water_damage"
    }

    for keyword, value in damage_keywords.items():
        if keyword in text:
            issue_type = value

    parts = [
        "screen",
        "bumper",
        "door",
        "hood",
        "keyboard",
        "package"
    ]

    for part in parts:
        if part in text:
            object_part = part

    return {
        "issue_type": issue_type,
        "object_part": object_part
    }