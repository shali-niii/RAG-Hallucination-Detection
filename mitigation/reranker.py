```python
"""
Evidence Reranking for RAG Hallucination Mitigation

Purpose:
    Reorder retrieved evidence passages according to their relevance
    to a user's question.

Model:
    cross-encoder/ms-marco-MiniLM-L-6-v2

Note:
    This component ranks evidence by relevance. It does not independently
    determine whether evidence is factually correct or supports a claim.
"""

from typing import Any, Dict, List

from sentence_transformers import CrossEncoder


DEFAULT_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"


class EvidenceReranker:
    """Rank retrieved evidence passages for a given question."""

    def __init__(self, model_name: str = DEFAULT_MODEL):
        """Initialize the cross-encoder relevance model."""
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        question: str,
        evidence: List[Dict[str, Any]],
        top_k: int = None,
    ) -> List[Dict[str, Any]]:
        """
        Rank evidence passages by relevance to a question.

        Args:
            question: The user's question.
            evidence: List of dictionaries containing a 'text' field.
            top_k: Maximum number of passages to return.
                   If None, return all passages.

        Returns:
            Evidence dictionaries sorted by descending relevance score.
            Original fields are preserved, and 'rerank_score' is added.
        """
        if not question or not question.strip():
            raise ValueError("Question must not be empty.")

        if top_k is not None and top_k < 0:
            raise ValueError("top_k must be zero or greater.")

        if not evidence:
            return []

        for index, passage in enumerate(evidence):
            if not isinstance(passage, dict):
                raise TypeError(
                    f"Evidence item {index} must be a dictionary."
                )

            if not isinstance(passage.get("text"), str):
                raise ValueError(
                    f"Evidence item {index} must contain a string 'text' field."
                )

        if top_k == 0:
            return []

        pairs = [
            (question, passage["text"])
            for passage in evidence
        ]

        scores = self.model.predict(pairs)

        ranked_evidence = []

        for passage, score in zip(evidence, scores):
            ranked_passage = dict(passage)
            ranked_passage["rerank_score"] = float(score)
            ranked_evidence.append(ranked_passage)

        ranked_evidence.sort(
            key=lambda item: item["rerank_score"],
            reverse=True,
        )

        if top_k is not None:
            ranked_evidence = ranked_evidence[:top_k]

        return ranked_evidence


if __name__ == "__main__":
    # Example input for a basic manual test.
    question = "Why does water boil at a lower temperature at high altitudes?"

    sample_evidence = [
        {
            "id": "E1",
            "text": "Water boils at a lower temperature when atmospheric pressure decreases.",
            "source": "example_document_1",
        },
        {
            "id": "E2",
            "text": "Mountain environments can have different vegetation and climates.",
            "source": "example_document_2",
        },
        {
            "id": "E3",
            "text": "Atmospheric pressure generally decreases as altitude increases.",
            "source": "example_document_3",
        },
    ]

    reranker = EvidenceReranker()
    results = reranker.rerank(question, sample_evidence, top_k=3)

    for item in results:
        print(f"ID: {item['id']}")
        print(f"Score: {item['rerank_score']:.4f}")
        print(f"Evidence: {item['text']}")
        print(f"Source: {item['source']}")
        print("-" * 50)
```
