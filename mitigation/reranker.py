# Evidence Reranking for Hallucination Mitigation

## 1. Overview

Evidence reranking is a technique used in Retrieval-Augmented Generation (RAG) systems to improve the relevance of retrieved documents before generating an answer.

A RAG system retrieves passages from a knowledge source and provides them to a language model. However, the initial retrieval results may contain irrelevant or less useful passages. If the model relies on weak evidence, it may generate unsupported claims.

Evidence reranking reorders the retrieved passages so that the most relevant passages appear first.

## 2. Objective

The objective is to improve the quality of evidence provided to the language model and reduce claims that are unsupported by the retrieved evidence.

## 3. How It Works

1. The user submits a question.
2. The retrieval system finds potentially relevant passages.
3. A reranking method scores the retrieved passages based on their relevance to the question.
4. The passages are reordered by their reranking scores.
5. The highest-ranked passages are passed to the language model.
6. The generated answer is evaluated against the evidence.

## 4. Example

**Question:** What is the main function of the human heart?

**Retrieved passage A:** The heart pumps blood throughout the body.

**Retrieved passage B:** The human stomach helps digest food.

For this question, passage A is more relevant than passage B. A reranking method should place passage A first.

This example illustrates relevance ranking; it does not demonstrate an experimentally measured reduction in hallucinations.

## 5. Expected Benefits

* Places more relevant evidence near the beginning of the context.
* Reduces the influence of irrelevant retrieved passages.
* May improve the factual grounding of generated answers.
* Provides a method that can be compared with baseline RAG.

## 6. Limitations

* Reranking cannot create evidence that was never retrieved.
* A highly ranked passage may still be incorrect or insufficient.
* Better retrieval relevance does not guarantee a truthful answer.
* Reranking may increase processing time.

## 7. Evaluation

Compare the baseline RAG system with the reranked system using the same test questions.

Measure:

* Claim support rate.
* Unsupported claim rate.
* Contradiction rate.
* Answer quality.

Use the same metric definitions for both systems. Report actual results only after running the experiments.

## 8. Integration With the Project

The reranking method should operate on the passages returned by the team's retrieval component. Its output should be passed to the RAG generation component.

The implementation should follow the data format agreed upon by the team.
