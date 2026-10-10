
from metrics import calculate_metrics


def main():
    # Example labels for testing the evaluation code.
    # Later, replace these with labels from your team's detector.
    example_labels = [
        "supported",
        "supported",
        "contradicted",
        "unverifiable",
    ]

    results = calculate_metrics(example_labels)

    print("RAG Hallucination Evaluation Results")
    print("------------------------------------")
    print(f"Total claims: {results['total_claims']}")
    print(f"Claim support rate: {results['claim_support_rate']:.2f}%")
    print(f"Unsupported claim rate: {results['unsupported_claim_rate']:.2f}%")
    print(f"Contradiction rate: {results['contradiction_rate']:.2f}%")
    print(f"Unverifiable rate: {results['unverifiable_rate']:.2f}%")


if __name__ == "__main__":
    main()
