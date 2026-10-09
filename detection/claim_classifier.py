def classify_claim(nli_result, similarity_score):
    """
    Combine NLI verification and semantic similarity
    to assign a final status to a factual claim.

    Returns:
        supported
        contradicted
        unverifiable
    """

    if not nli_result:
        return "unverifiable"

    label = nli_result.get("label", "neutral")
    confidence = float(nli_result.get("confidence", 0.0))

    # Strong contradiction takes priority.
    if label == "contradiction" and confidence >= 0.60:
        return "contradicted"

    # Strong entailment with reasonable semantic overlap.
    if (
        label == "entailment"
        and confidence >= 0.60
        and similarity_score >= 0.45
    ):
        return "supported"

    # A very low semantic relationship should not be
    # treated as supported even if the NLI model is uncertain.
    if similarity_score < 0.25:
        return "unverifiable"

    return "unverifiable"


def explain_classification(status):
    explanations = {
        "supported": "The evidence provides support for the claim.",
        "contradicted": "The evidence conflicts with the claim.",
        "unverifiable": "The available evidence does not sufficiently establish the claim."
    }

    return explanations.get(
        status,
        "The claim could not be classified."
    )


if __name__ == "__main__":
    sample_nli = {
        "label": "entailment",
        "confidence": 0.91
    }

    sample_similarity = 0.78

    result = classify_claim(
        sample_nli,
        sample_similarity
    )

    print("Claim Classification")
    print("--------------------")
    print(f"Status: {result}")
    print(f"Reason: {explain_classification(result)}")