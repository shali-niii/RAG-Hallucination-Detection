# Claim-Level Self-Verification

## 1. Overview

Claim-level self-verification is a hallucination mitigation technique that checks individual factual claims in a generated answer against the evidence retrieved by a Retrieval-Augmented Generation (RAG) system.

An answer may contain several claims, some supported by the evidence and others unsupported or contradicted. Evaluating each claim separately helps identify which statements need correction or removal.

## 2. Objective

The objective is to improve answer reliability by identifying unsupported claims before the final answer is returned to the user.

## 3. Methodology

The technique follows these steps:

1. Receive the question, generated answer, and retrieved evidence passages.
2. Split the answer into individual factual claims.
3. Compare each claim with the relevant evidence.
4. Assign a verification label to each claim:

   * **Supported:** The evidence supports the claim.
   * **Contradicted:** The evidence conflicts with the claim.
   * **Unverifiable:** The available evidence is insufficient to determine whether the claim is correct.
5. Identify claims that require correction, removal, or additional evidence.
6. Produce a revised answer that retains supported claims and avoids presenting unsupported claims as facts.
7. Recheck the revised answer when the verification component is available.

## 4. Expected Input

* The original user question.
* The generated answer.
* Retrieved evidence passages with source identifiers.
* A claim extraction and verification component.

## 5. Expected Output

The component should provide:

* Extracted claims.
* A verification label for each claim.
* The evidence associated with each claim.
* A revised answer that avoids unsupported statements.

## 6. Role in Hallucination Mitigation

Claim-level self-verification complements evidence reranking and citation-constrained generation.

Evidence reranking prioritizes relevant passages, citation-constrained generation encourages answers to reference evidence, and self-verification checks whether individual claims are supported by that evidence.

These techniques address different stages of the RAG pipeline and can be evaluated separately and together.

## 7. Evaluation

The technique can be evaluated using:

* Claim support rate.
* Unsupported claim rate.
* Contradicted claim rate.
* Factual consistency between the answer and retrieved evidence.
* Answer quality and completeness after mitigation.

Experiments should compare baseline answers with answers produced after self-verification. Any improvements must be established using measured results rather than assumed.

## 8. Limitations

Verification quality depends on the quality of claim extraction, retrieved evidence, and the verification model. Incorrect labels may cause valid information to be removed or unsupported claims to remain.

A claim classified as unverifiable is not necessarily false; it may simply lack sufficient evidence in the retrieved passages.

## 9. Conclusion

Claim-level self-verification provides a structured way to identify and mitigate unsupported statements in RAG-generated answers. In this project, it will be evaluated alongside evidence reranking and citation-constrained generation to measure its contribution to reducing hallucinations.
