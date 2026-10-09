from claim_extractor import extract_claims
from nli import NLIEngine
from similarity import SimilarityEngine
from claim_classifier import classify_claim, explain_classification
from hallucination_score import calculate_hallucination_score


class HallucinationDetector:

    def __init__(self):
        print("Loading detection models...")

        self.nli_engine = NLIEngine()
        self.similarity_engine = SimilarityEngine()

        print("Models loaded successfully.\n")

    def analyze(self, answer, evidence):

        claims = extract_claims(answer)

        if not claims:
            return {
                "claims": [],
                "hallucination_score": 0.0
            }

        results = []

        for number, claim in enumerate(claims, start=1):

            nli_result = self.nli_engine.verify(
                claim,
                evidence
            )

            similarity_score = self.similarity_engine.score(
                claim,
                evidence
            )

            status = classify_claim(
                nli_result,
                similarity_score
            )

            results.append({
                "claim_number": number,
                "claim": claim,
                "nli_label": nli_result["label"],
                "nli_confidence": nli_result["confidence"],
                "similarity": similarity_score,
                "status": status,
                "explanation": explain_classification(status)
            })

        classifications = [
            result["status"]
            for result in results
        ]

        overall_score = calculate_hallucination_score(
            classifications
        )

        return {
            "claims": results,
            "hallucination_score": overall_score
        }


if __name__ == "__main__":

    answer = (
        "The Eiffel Tower is located in London. "
        "It was completed in 1889."
    )

    evidence = (
        "The Eiffel Tower is located in Paris, France. "
        "Construction was completed in 1889."
    )

    detector = HallucinationDetector()

    report = detector.analyze(
        answer,
        evidence
    )

    print("Hallucination Detection Report")
    print("==============================")

    for result in report["claims"]:

        print(f"\nClaim {result['claim_number']}:")
        print(f"  {result['claim']}")
        print(f"  NLI           : {result['nli_label']}")
        print(f"  NLI confidence: {result['nli_confidence']}")
        print(f"  Similarity    : {result['similarity']}")
        print(f"  Status        : {result['status']}")
        print(f"  Explanation   : {result['explanation']}")

    print("\n------------------------------")
    print(
        f"Overall hallucination score: "
        f"{report['hallucination_score']}"
    )