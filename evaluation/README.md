# Evaluation of RAG Hallucinations

## Overview

This folder contains the evaluation plan for our project, **Evaluating and Mitigating Hallucinations in Retrieval-Augmented Large Language Models**.

The goal is to measure whether mitigation methods reduce hallucinations while maintaining answer quality.

## What We Will Evaluate

We will compare the original RAG system with versions that use different mitigation methods:

1. **Baseline RAG:** The original system without additional mitigation.
2. **Evidence Reranking:** Reordering retrieved passages so that more relevant evidence appears first.
3. **Citation-Constrained Generation:** Encouraging the model to support its claims with retrieved evidence.
4. **Claim-Level Self-Verification:** Checking individual claims and revising claims that are unsupported or contradicted by the evidence.
5. **Combined Mitigation (optional):** Combining the methods to examine whether they work better together.

## Evaluation Metrics

We plan to measure:

* **Claim Support Rate:** The proportion of evaluated claims supported by the retrieved evidence.
* **Unsupported Claim Rate:** The proportion of claims that lack sufficient supporting evidence.
* **Contradiction Rate:** The proportion of claims that conflict with the evidence.
* **Answer Quality:** How relevant, clear, and useful the answers are.

We will report unsupported and contradicted claims separately so that the results are clear.

## Experimental Procedure

1. Use the same test questions for each system configuration.
2. Record the answers and evidence produced by each configuration.
3. Evaluate claims against the available evidence.
4. Calculate the evaluation metrics using the same definitions for each configuration.
5. Compare the baseline results with the mitigation results.
6. Review a sample of automatic labels manually, where possible.

## Expected Outcome

We expect effective mitigation methods to reduce unsupported and contradicted claims without substantially reducing answer quality. This is a hypothesis to test, not a confirmed result.

## Limitations

* Automatic claim evaluation can make mistakes.
* Retrieved evidence may be incomplete or irrelevant.
* Citation presence does not guarantee that a claim is supported.
* Answer quality can be partly subjective.

Actual results will be documented after the experiments have been run.
