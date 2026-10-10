# Citation-Constrained Generation

## 1. Overview

Citation-constrained generation is a hallucination mitigation technique used in Retrieval-Augmented Generation (RAG) systems. It encourages a language model to generate answers that are grounded in retrieved evidence and provide citations for factual claims.

Even when a RAG system retrieves relevant documents, a language model may produce unsupported statements or cite sources that do not support its claims. This technique aims to improve answer traceability and reduce unsupported statements.

## 2. Objective

The objective is to generate answers in which factual claims are supported by the available evidence and linked to the relevant evidence sources.

## 3. Methodology

The technique follows these steps:

1. Receive the user's question and the evidence passages retrieved by the RAG system.
2. Provide the question and evidence to the language model.
3. Instruct the model to answer using the supplied evidence.
4. Require citations that refer to the identifiers of the supplied evidence passages.
5. Instruct the model to state when the evidence is insufficient instead of inventing information.
6. Return the generated answer with its citations for further verification.

## 4. Expected Input

* A user question.
* A collection of evidence passages.
* A unique identifier or source reference for each passage.

## 5. Expected Output

An answer containing factual statements linked to evidence identifiers or source references.

If the supplied evidence is insufficient, the system should indicate that limitation rather than present unsupported information as fact.

## 6. Role in Hallucination Mitigation

Citation-constrained generation aims to improve the connection between generated claims and retrieved evidence. It also makes answers easier to inspect because readers can trace claims to their sources.

However, adding a citation does not guarantee that a claim is correct or that the cited evidence actually supports it. The citations and claims should therefore be checked by the project's claim-level verification component.

## 7. Evaluation

The technique can be evaluated using measures such as:

* Citation coverage: the proportion of eligible factual claims that have citations.
* Citation correctness: the proportion of evaluated citations that refer to evidence supporting their associated claims.
* Claim support rate: the proportion of evaluated factual claims supported by the available evidence.
* Hallucination rate: the proportion of evaluated claims classified as unsupported or contradicted, according to the project's evaluation protocol.

The evaluation should compare baseline RAG answers with answers produced using citation-constrained generation. Actual results must be measured experimentally.

## 8. Limitations

The technique depends on the quality and completeness of the supplied evidence. A model may still misinterpret evidence, omit citations, or attach an irrelevant citation to a claim. Additional claim-level verification is therefore necessary.

## 9. Conclusion

Citation-constrained generation is a mitigation technique that encourages evidence-grounded answers and traceable citations. In this project, it will be evaluated as one component of a broader framework for detecting and mitigating hallucinations in RAG systems.
