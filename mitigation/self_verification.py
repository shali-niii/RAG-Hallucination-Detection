"""
Claim-level self-verification for RAG hallucination mitigation.

Extracts claims, verifies them against retrieved evidence using a
supplied verifier, and builds a revised answer from supported claims.
"""

from typing import Any, Callable, Dict, List


VALID_LABELS = {"supported", "contradicted", "unverifiable"}


def verify_claims(
    claims: List[str],
    evidence: List[Dict[str, Any]],
    verifier: Callable[[str, List[Dict[str, Any]]], Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Verify individual claims against retrieved evidence.

    Args:
        claims: Factual claims extracted from a generated answer.
        evidence: Evidence dictionaries, typically containing 'id',
                  'text', and optionally 'source'.
        verifier: A function that accepts a claim and evidence list,
                  and returns a dictionary containing a 'label'.

    Returns:
        One verification result per claim.
    """
    results = []

    for claim in claims:
        result = verifier(claim, evidence)
        label = str(result.get("label", "unverifiable")).lower()

        if label not in VALID_LABELS:
            label = "unverifiable"

        results.append(
            {
                "claim": claim,
                "label": label,
                "evidence": result.get("evidence", []),
                "reason": result.get(
                    "reason", "No verification explanation provided."
                ),
            }
        )

    return results


def build_revised_answer(
    verification_results: List[Dict[str, Any]],
    include_unverifiable: bool = False,
) -> str:
    """
    Build a cautious answer using verification results.

    By default, only supported claims are retained. Unverifiable claims
    can optionally be retained with an explicit uncertainty marker.
    Contradicted claims are excluded.
    """
    revised_claims = []

    for result in verification_results:
        label = result.get("label", "unverifiable")
        claim = str(result.get("claim", "")).strip()

        if not claim:
            continue

        if label == "supported":
            revised_claims.append(claim)

        elif label == "unverifiable" and include_unverifiable:
            revised_claims.append(
                f"{claim} (This claim could not be verified from the available evidence.)"
            )

    if not revised_claims:
        return (
            "The available evidence does not sufficiently support "
            "a reliable answer."
        )

    return " ".join(revised_claims)


def self_verify_answer(
    answer: str,
    evidence: List[Dict[str, Any]],
    claim_extractor: Callable[[str], List[str]],
    verifier: Callable[[str, List[Dict[str, Any]]], Dict[str, Any]],
    include_unverifiable: bool = False,
) -> Dict[str, Any]:
    """
    Extract claims, verify them, and produce a revised answer.

    Args:
        answer: Original LLM-generated answer.
        evidence: Retrieved evidence passages.
        claim_extractor: A function that extracts factual claims from
                         the answer and returns a list of strings.
        verifier: A function that labels each claim using the evidence.
        include_unverifiable: Whether to retain uncertain claims with
                              an explicit warning.

    Returns:
        Original answer, extracted claims, verification results,
        and revised answer.
    """
    claims = claim_extractor(answer)

    results = verify_claims(
        claims=claims,
        evidence=evidence,
        verifier=verifier,
    )

    revised_answer = build_revised_answer(
        verification_results=results,
        include_unverifiable=include_unverifiable,
    )

    return {
        "original_answer": answer,
        "claims": claims,
        "verification_results": results,
        "revised_answer": revised_answer,
    }
