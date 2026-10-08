import re


def extract_claims(answer):
    """
    Convert a generated answer into individual factual claims.

    This is a lightweight first-stage extractor.
    It keeps sentence splitting simple so that the output
    can later be passed to the verification modules.
    """

    if not answer or not answer.strip():
        return []

    # Normalize unnecessary whitespace
    cleaned = re.sub(r"\s+", " ", answer.strip())

    # Split after sentence-ending punctuation.
    pieces = re.split(r"(?<=[.!?])\s+", cleaned)

    claims = []

    for piece in pieces:
        claim = piece.strip()

        if not claim:
            continue

        # Remove trailing punctuation for cleaner processing
        claim = claim.rstrip(".!?").strip()

        if len(claim) >= 3:
            claims.append(claim)

    return claims


if __name__ == "__main__":
    sample_answer = (
        "The Eiffel Tower is located in Paris. "
        "It was completed in 1889."
    )

    extracted = extract_claims(sample_answer)

    print("Extracted Claims")
    print("----------------")

    for number, claim in enumerate(extracted, start=1):
        print(f"{number}. {claim}")