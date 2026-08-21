# RAG-for-Biomedical-Question-Answering

Course project for **Deep Learning** at the **University of Ljubljana**.

This project implements and evaluates a small **Retrieval-Augmented Generation (RAG)** pipeline for biomedical question answering. The goal is to investigate whether providing a language model with relevant passages retrieved from medical textbooks improves its performance compared with answering questions without retrieval.

The system is evaluated on questions from **MedMCQA** and compares a baseline LLM with the same model augmented with retrieved textbook context.

## System

* **LLM:** Qwen2.5-1.5B-Instruct
* **Retrieval:** Sentence Transformers + FAISS
* **Knowledge base:** Medical textbooks
* **Evaluation dataset:** MedMCQA

For each question, the system retrieves relevant passages from the medical textbook corpus using semantic similarity. These passages are then provided to the language model as additional context for answering the question.

## Pipeline

```text
Medical textbooks
       │
       ▼
Sentence Transformer embeddings
       │
       ▼
    FAISS index
       │
       ▼
MedMCQA question ──► Semantic retrieval
                         │
                         ▼
                Top-k textbook passages
                         │
                         ▼
                Qwen2.5-1.5B-Instruct
                         │
                         ▼
                  Predicted answer
                         │
                         ▼
               Evaluation & analysis
```

Two main settings are compared:

1. **Baseline** – the model answers the question without retrieved textbook context.
2. **RAG** – the model receives the top-k retrieved textbook passages as additional context.


## Main Files

### RAG pipeline

* **`RAG.py`** – main RAG and evaluation pipeline. It loads the global experiment parameters from `config.json`, retrieves relevant textbook passages, generates answers using Qwen, and evaluates the predictions.

* **`config.json`** – configuration file containing the parameters used by the RAG pipeline.


### Analysis

* **`analysis.py`** – processes experiment outputs and generates files used for further analysis of the RAG results.

* **`analysis_of_500_questions/`** – contains detailed results and manual error analysis for experiments on 500 MedMCQA questions.


## Analysis of 500 Questions

The `analysis_of_500_questions/` directory contains results and error analysis for a subset of **500 MedMCQA questions**. It compares baseline and RAG predictions and examines cases where retrieval either **corrected an incorrect baseline answer or changed a correct answer into an incorrect one**. These cases were manually reviewed to determine whether relevant information was present in the retrieved documents and to better understand the source of the errors.

## Report
A detailed description of the methodology, experiments, results, and analysis can be found in the [**project report**](./report.pdf).
