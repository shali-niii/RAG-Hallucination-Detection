# Hallucination Mitigation Methods

## Overview

This folder describes methods for reducing hallucinations in our Retrieval-Augmented Generation (RAG) system.

A hallucination occurs when a model produces a claim that is unsupported by, or contradicts, the available evidence.

Our goal is to reduce unsupported claims while maintaining answer quality.

## 1. Evidence Reranking

Evidence reranking reorders retrieved passages so that the most relevant evidence appears earlier.

**Purpose:**

* Help the model focus on useful evidence.
* Reduce answers based on irrelevant or weakly related passages.

**Evaluation:**
Compare the baseline RAG system with the reranked system using the same test questions. Measure claim support, unsupported claims, contradictions, and answer quality.

## 2. Citation-Constrained Generation

Citation-constrained generation encourages the model to support its claims using the retrieved passages.

**Purpose:**

* Make it easier to trace claims back to evidence.
* Identify claims that lack supporting passages.

**Important limitation:**
A citation alone does not prove that a claim is correct. The cited passage must actually support the claim.

**Evaluation:**
Check whether claims are supported by their cited evidence and measure unsupported claims, contradictions, and answer quality.

## 3. Claim-Level Self-Verification

Claim-level self-verification checks individual claims in a generated answer against the available evidence.

**Purpose:**

* Identify unsupported or contradicted claims.
* Revise or remove claims that cannot be justified by the evidence.
* Reduce unsupported statements in the final answer.

**Evaluation:**
Compare the original answer with the verified answer using the same test questions and evaluation metrics.

## Experimental Comparison

We plan to compare:

1. Baseline RAG without additional mitigation.
2. RAG with evidence reranking.
3. RAG with citation-constrained generation.
4. RAG with claim-level self-verification.
5. A combined system, if time and implementation allow.

All configurations should use the same test questions and consistent metric definitions.

## Expected Outcome

We expect effective mitigation methods to reduce unsupported and contradicted claims without substantially reducing answer quality. This is a hypothesis, not a confirmed result.

Actual results should be added only after the experiments have been run.

## Coordination With Other Project Components

* The RAG component provides questions, retrieved passages, and generated answers.
* The detection component identifies and labels claims against the evidence.
* The evaluation component compares results across baseline and mitigation configurations.

The mitigation methods should use the project's agreed data format and integrate with the team's actual implementation.
