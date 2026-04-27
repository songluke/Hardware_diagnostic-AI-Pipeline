# Hardware Diagnostic & Failure Analysis AI Pipeline

## Overview
This project is an advanced, offline-capable AI infrastructure developed to streamline the Failure Analysis (FA) workflow. By integrating **Large Language Models (LLMs)** with structured and unstructured hardware datasets, this pipeline enables engineers to perform complex diagnostics using natural language, significantly reducing the time required to identify recurring failure patterns.

## Key Technical Solutions

### 1. Natural Language to SQL Translation
- **Challenge:** FA data is often siloed in relational databases, requiring specific SQL knowledge to query.
- **Solution:** Implemented a schema-aware translation layer using **Llama 3** that converts engineering requests into optimized SQLite queries.
- **Result:** Direct access to structured failure telemetry without manual query writing.

### 2. Privacy-First Retrieval-Augmented Generation (RAG)
- **Challenge:** Proprietary engineering logs and case studies cannot be uploaded to third-party cloud APIs due to strict data sovereignty policies.
- **Solution:** Built a local knowledge retrieval system using **Ollama** and **ChromaDB**. This ensures all data processing remains on-premises and air-gapped.
- **Result:** Automated root cause analysis (RCA) summaries generated from unstructured technical logs.



## System Architecture
* **Inference Engine:** Llama 3 (running locally via Ollama)
* **Vector Embeddings:** Nomic-Embed-Text
* **Database Layer:** SQLite (Structured) & ChromaDB (Unstructured)
* **Application Framework:** Streamlit

## Security & Intellectual Property
To demonstrate the architectural logic while maintaining corporate confidentiality, this public portfolio version utilizes **synthetic hardware datasets** and **anonymized failure modes**. The system logic, prompt orchestration, and retrieval workflows are identical to production-grade implementations.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Ensure Ollama is running locally with the `llama3` model.
4. Run the application: `streamlit run app.py`.

---
**Developed by Luke Song**
