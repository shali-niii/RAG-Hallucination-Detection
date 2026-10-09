from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:
    """
    Calculates semantic similarity between claims and evidence
    using sentence embeddings and cosine similarity.
    """

    def __init__(self):
        self.encoder = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def score(self, claim, evidence):
        if not claim or not evidence:
            return 0.0

        vectors = self.encoder.encode(
            [claim, evidence],
            normalize_embeddings=True
        )

        claim_vector = vectors[0].reshape(1, -1)
        evidence_vector = vectors[1].reshape(1, -1)

        similarity = cosine_similarity(
            claim_vector,
            evidence_vector
        )[0][0]

        # Convert possible tiny floating-point deviations
        # into a clean range.
        similarity = max(0.0, min(1.0, float(similarity)))

        return round(similarity, 4)


if __name__ == "__main__":
    engine = SimilarityEngine()

    claim = "The Eiffel Tower is in Paris."
    evidence = "The Eiffel Tower is located in Paris, France."

    score = engine.score(claim, evidence)

    print("Semantic Similarity")
    print("-------------------")
    print(f"Claim    : {claim}")
    print(f"Evidence : {evidence}")
    print(f"Score    : {score}")