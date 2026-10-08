# RAG-Hallucination-Detection
Research project on detecting and mitigating hallucinations in RAG systems through claim-level verification, NLI, semantic similarity, and evidence-based generation.
Day

# Evaluating and Mitigating Hallucinations in Retrieval-Augmented Large Language Models

> Research project on detecting and mitigating hallucinations in Retrieval-Augmented Generation (RAG) systems through claim-level verification, Natural Language Inference (NLI), semantic similarity, and evidence-based generation.

---

## 📌 Overview

Retrieval-Augmented Generation (RAG) improves the factual reliability of Large Language Models (LLMs) by providing relevant external context. However, RAG systems can still produce hallucinations, including unsupported claims, misattributed evidence, and answers that contradict or ignore the retrieved context.

This project proposes a framework to detect and mitigate hallucinations at the **claim level** by separating:

- **Retrieval-stage failures** — irrelevant, incomplete, or conflicting retrieved evidence.
- **Generation-stage failures** — unfaithful synthesis or unsupported extrapolation.

Each generated answer is decomposed into individual factual claims. These claims are then compared against the retrieved evidence using **NLI** and **semantic similarity** and classified as:

- ✅ Supported
- ❌ Contradicted
- ⚠️ Unverifiable

The framework then applies mitigation strategies such as evidence reranking, citation-constrained generation, and claim-level self-verification.

---

## 🎯 Objectives

1. Build a baseline Retrieval-Augmented Generation (RAG) system.
2. Identify retrieval-stage and generation-stage failure cases.
3. Decompose generated answers into individual factual claims.
4. Verify claims against retrieved evidence using NLI and semantic similarity.
5. Classify claims as supported, contradicted, or unverifiable.
6. Apply mitigation techniques to reduce hallucinations.
7. Compare baseline RAG with the proposed mitigation strategies.
8. Provide explainable hallucination detection by tracing claims back to their evidence.

---

## 🔬 Research Methodology

```text
Documents
    ↓
Preprocessing & Chunking
    ↓
Embeddings / Vector Database
    ↓
Retriever
    ↓
Retrieved Evidence
    ↓
RAG / LLM
    ↓
Generated Answer
    ↓
Claim Extraction
    ↓
NLI + Semantic Similarity
    ↓
Claim Classification
    ↓
Supported / Contradicted / Unverifiable
    ↓
Mitigation
    ↓
Regenerated Answer
    ↓
Evaluation

## 📅 4-Day Work Plan

| Day | Shalini — RAG & Retrieval | Sukant — Hallucination Detection | Manushri — Mitigation & Evaluation | Team Target |
|---|---|---|---|---|
| **Day 1 — Oct 8** | Finalize dataset/domain; collect documents; preprocessing; chunking; start embeddings & vector DB; create initial questions | Decide claim extraction, NLI & similarity models; create sample claims; start claim extraction + NLI prototype | Define evaluation metrics; design experiments; set up evaluation structure | Finalize dataset, models, common JSON format & Git workflow |
| **Day 2 — Oct 9** | Complete embeddings, vector DB, retriever & baseline RAG; generate initial test set | Complete claim extraction, NLI, similarity & classification | Implement reranking, citation-constrained generation & self-verification; connect evaluation | **Working end-to-end baseline:** RAG → Claims → NLI + Similarity → Labels |
| **Day 3 — Oct 10** | Run baseline on full test set; analyze retrieval failures; finalize evidence/answer dataset | Run claim-level detection; calculate hallucination metrics; perform error analysis | Run baseline + mitigation experiments; generate graphs/tables/results | **Final experimental results + comparison** |
| **Day 4 — Oct 11** | Prepare RAG architecture, dataset & retrieval slides | Prepare hallucination detection, NLI & similarity slides | Prepare mitigation, evaluation & results slides | Final PPT, paper review, GitHub cleanup & presentation rehearsal |

## 👥 Team Responsibilities

| Member | Primary Folders | Main Responsibility | Expected Output |
|---|---|---|---|
| **Shalini** | `data/`, `rag/`, `generator/` | Dataset, preprocessing, retrieval, baseline RAG & test generation | Question → Retrieved Evidence → Generated Answer |
| **Sukant** | `detection/` | Claim extraction, NLI, semantic similarity & hallucination classification | Claim → Evidence → Detection Label |
| **Manushri** | `mitigation/`, `evaluation/`, `experiments/` | Mitigation techniques, evaluation & experiments | Baseline → Mitigation → Improved Answer → Results |
| **All Members** | `paper/`, `README.md` | Integration, paper, PPT, testing & presentation | Final Paper + PPT + GitHub Repository |

## 🔄 End-to-End Pipeline

```text
Question
   ↓
Document Retrieval
   ↓
Retrieved Evidence
   ↓
RAG / LLM
   ↓
Generated Answer
   ↓
Claim Extraction
   ↓
NLI + Semantic Similarity
   ↓
Supported / Contradicted / Unverifiable
   ↓
Mitigation
   ↓
Regenerated Answer
   ↓
Evaluation
