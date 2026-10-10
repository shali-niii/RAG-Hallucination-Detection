"""
Citation-constrained generation for RAG hallucination mitigation.

Builds prompts that encourage an LLM to answer using retrieved evidence
and cite the evidence supporting its factual claims.
"""

from typing import Any, Callable, Dict, List


def format_evidence(evidence: List[Dict[str, Any]]) -> str:
    """Format evidence passages with unique identifiers for citation."""

    if not evidence:
        return "No evidence passages were provided."

    formatted_passages = []

    for index, item in enumerate(evidence, start=1):
        evidence_id = str(item.get("id", f"E{index}"))
        text = str(item.get("text", "")).strip()
        source = str(item.get("source", "Unknown source"))

        formatted_passages.append(
            f"[{evidence_id}]\n"
            f"Source: {source}\n"
            f"Content: {text}"
        )

    return "\n\n".join(formatted_passages)


def build_citation_prompt(
    question: str,
    evidence: List[Dict[str, Any]],
) -> str:
    """Build a prompt that requires evidence-grounded answers."""

    evidence_text = format_evidence(evidence)

    return f"""
You are an assistant answering questions using retrieved evidence.

Rules:
1. Answer the question using only the evidence provided below.
2. Cite evidence for factual claims using its exact identifier,
   for example [E1].
3. Do not invent evidence identifiers or sources.
4. If the evidence does not support an answer, clearly state that
   the available evidence is insufficient.
5. If only part of the question can be answered, explain which
   part is supported and which part remains uncertain.
6. Do not treat a citation as proof unless the evidence supports
   the associated claim.

Question:
{question}

Retrieved evidence:
{evidence_text}

Write a concise answer with citations:
""".strip()


def generate_cited_answer(
    question: str,
    evidence: List[Dict[str, Any]],
    generate_text: Callable[[str], str],
) -> Dict[str, Any]:
    """
    Generate an answer using a supplied language-model function.

    Args:
        question: The user's question.
        evidence: Evidence dictionaries with 'text' and optional
                  'id' and 'source' fields.
        generate_text: A callable that accepts a prompt and returns
                       generated text from an LLM.

    Returns:
        A dictionary containing the answer, prompt, and evidence.

    Note:
        This function encourages citations but does not independently
        verify that the answer or citations are correct.
    """

    prompt = build_citation_prompt(question, evidence)
    answer = generate_text(prompt)

    return {
        "question": question,
        "answer": answer,
        "evidence": evidence,
        "prompt": prompt,
    }
