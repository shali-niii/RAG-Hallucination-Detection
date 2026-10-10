
def calculate_metrics(claim_labels):
    """
    Calculate evaluation metrics from claim labels.

    Valid labels:
    - supported
    - contradicted
    - unverifiable

    Example:
    ["supported", "supported", "contradicted", "unverifiable"]
    """

    valid_labels = {"supported", "contradicted", "unverifiable"}

    # Normalize labels and remove extra spaces.
    labels = [str(label).strip().lower() for label in claim_labels]

    # Reject labels that are not recognized.
    invalid_labels = set(labels) - valid_labels
    if invalid_labels:
        raise ValueError(f"Unknown claim labels: {sorted(invalid_labels)}")

    total = len(labels)

    # Avoid division by zero when there are no claims.
    if total == 0:
        return {
            "total_claims": 0,
            "claim_support_rate": 0.0,
            "unsupported_claim_rate": 0.0,
            "contradiction_rate": 0.0,
            "unverifiable_rate": 0.0,
        }

    supported = labels.count("supported")
    contradicted = labels.count("contradicted")
    unverifiable = labels.count("unverifiable")

    return {
        "total_claims": total,
        "claim_support_rate": supported / total * 100,
        "unsupported_claim_rate": unverifiable / total * 100,
        "contradiction_rate": contradicted / total * 100,
        "unverifiable_rate": unverifiable / total * 100,
    }
