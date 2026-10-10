# Evaluation Metrics

## Purpose

This document defines the metrics used to evaluate hallucinations in our Retrieval-Augmented Generation (RAG) system.

We will use these metrics to compare the baseline system with systems that use hallucination mitigation methods.

## 1. Claim Support Rate

Measures the percentage of evaluated claims labelled as supported by the available evidence.

**Formula:**

Claim Support Rate = (Number of supported claims / Total number of evaluated claims) × 100

## 2. Unsupported Claim Rate

For our initial implementation, this metric counts claims labelled as unverifiable because the available evidence does not establish whether they are correct.

**Formula:**

Unsupported Claim Rate = (Number of unverifiable claims / Total number of evaluated claims) × 100

## 3. Contradiction Rate

Measures the percentage of evaluated claims that conflict with the available evidence.

**Formula:**

Contradiction Rate = (Number of contradicted claims / Total number of evaluated claims) × 100

## 4. Unverifiable Rate

Measures the percentage of claims for which the available evidence is insufficient to determine support or contradiction.

**Formula:**

Unverifiable Rate = (Number of unverifiable claims / Total number of evaluated claims) × 100

In this initial implementation, the unsupported claim rate and unverifiable rate are identical. We may revise these definitions if the team adopts a more detailed labelling scheme.

## Interpretation

* A higher claim support rate is generally desirable.
* Lower contradiction and unverifiable rates are generally desirable.
* Results should be interpreted alongside answer quality.
* Unverifiable does not mean false; it means the available evidence is insufficient.

## Evaluation Procedure

1. Use the same test questions for each system configuration.
2. Obtain claim labels from the project's claim detection component.
3. Calculate each metric using the same definitions.
4. Compare baseline and mitigation results.
5. Manually review a sample of labels when possible.

Actual results will be reported after the experiments have been conducted.
