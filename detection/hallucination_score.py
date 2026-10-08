def calculate_hallucination_score(classifications):
    """
    Calculate a hallucination score from claim-level results.

    Weighting:
        supported      -> 0.0
        unverifiable   -> 0.5
        contradicted   -> 1.0

    Final score:
        0.0 = no detected hallucination
        1.0 = all claims are detected as problematic
    """

    if not classifications:
        return 0.0

    penalty = {
        "supported": 0.0,
        "unverifiable": 0.5,
        "contradicted": 1.0
    }

    total = sum(
        penalty.get(item.lower(), 0.5)
        for item in classifications
    )

    score = total / len(classifications)

    return round(score, 4)


def describe_score(score):
    if score < 0.25:
        return "Low hallucination level"
    elif score < 0.50:
        return "Moderate hallucination level"
    elif score < 0.75:
        return "High hallucination level"
    else:
        return "Very high hallucination level"


if __name__ == "__main__":
    example_results = [
        "supported",
        "supported",
        "contradicted",
        "unverifiable"
    ]

    score = calculate_hallucination_score(example_results)

    print("Hallucination Analysis")
    print("----------------------")
    print(f"Score       : {score}")
    print(f"Interpretation: {describe_score(score)}")