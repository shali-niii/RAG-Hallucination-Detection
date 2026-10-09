from transformers import pipeline


class NLIEngine:
    """
    Natural Language Inference engine for claim verification.

    The model receives:
        premise  = retrieved evidence
        hypothesis = generated claim

    It predicts whether the evidence entails,
    contradicts, or is neutral toward the claim.
    """

    def __init__(self):
        self.model = pipeline(
            "text-classification",
            model="facebook/bart-large-mnli"
        )

    def verify(self, claim, evidence):
        if not claim or not evidence:
            return {
                "label": "neutral",
                "confidence": 0.0
            }

        result = self.model(
            f"{evidence} </s></s> {claim}",
            top_k=3
        )

        predictions = result[0] if isinstance(result[0], list) else result

        best = max(predictions, key=lambda item: item["score"])

        label_map = {
            "ENTAILMENT": "entailment",
            "CONTRADICTION": "contradiction",
            "NEUTRAL": "neutral"
        }

        label = label_map.get(
            best["label"].upper(),
            best["label"].lower()
        )

        return {
            "label": label,
            "confidence": round(float(best["score"]), 4)
        }


if __name__ == "__main__":
    verifier = NLIEngine()

    evidence = "The Eiffel Tower is located in Paris, France."
    claim = "The Eiffel Tower is in Paris."

    result = verifier.verify(claim, evidence)

    print("NLI Result")
    print("----------")
    print(f"Claim      : {claim}")
    print(f"Evidence   : {evidence}")
    print(f"Label      : {result['label']}")
    print(f"Confidence : {result['confidence']}")