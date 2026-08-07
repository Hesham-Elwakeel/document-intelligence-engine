# 📄 Document Intelligence Engine

A production-ready AI Document Intelligence Engine built with **FastAPI**, **Computer Vision**, **Large Language Models (LLMs)**, and **Vector Databases**.

The system is designed to understand, process, index, retrieve, and reason over documents using OCR, semantic embeddings, Retrieval-Augmented Generation (RAG), and modern AI engineering practices.

---

# 🚀 Project Goal

Build a scalable AI backend capable of:

* Uploading PDF and image documents
* Detecting document types automatically
* Extracting text from digital PDFs
* Performing OCR on scanned documents
* Classifying documents before processing
* Cleaning and preprocessing extracted text
* Splitting documents into semantic chunks
* Generating vector embeddings
* Storing embeddings in a Vector Database
* Semantic Search
* Retrieval-Augmented Generation (RAG)
* Question Answering over documents
* Document Summarization
* Structured JSON extraction

---

# 🛠 Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

## AI & Document Processing

* PyMuPDF
* PaddleOCR
* Sentence Transformers
* BAAI/bge-small-en-v1.5
* OpenAI API *(Planned)*

## Vector Database

* Qdrant *(In Progress)*

## Infrastructure

* Docker ✅
* Docker Compose *(Planned)*
* PostgreSQL *(Planned)*
* Redis *(Planned)*

---

# 📂 Project Structure

```text
document-intelligence-engine/

├── app/
│   ├── api/
│   ├── core/
│   ├── pipelines/
│   │   └── document_pipeline.py
│   │
│   ├── schemas/
│   │   ├── chunk.py
│   │   ├── document.py
│   │   ├── embedding.py
│   │   └── pipeline.py
│   │
│   ├── services/
│   │   ├── chunking_service.py
│   │   ├── document_classifier.py
│   │   ├── embedding_service.py
│   │   ├── file_service.py
│   │   ├── ocr_service.py
│   │   ├── pdf_service.py
│   │   └── text_cleaner.py
│   │
│   ├── utils/
│   └── main.py
│
├── data/
│   └── uploads/
│
├── docs/
├── tests/
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── README.md
└── .env.example
```

---

# 🔄 Processing Workflow

```text
Upload Document
        │
        ▼
Validate File Type
        │
        ▼
Save File
        │
        ▼
Detect File Type
        │
        ▼
Document Pipeline
        │
        ├──────────────────────┐
        ▼                      ▼
   PDF Pipeline          Image Pipeline
        │                      │
        ▼                      ▼
PDF Extraction           PaddleOCR
        │                      │
        └──────────────┬───────┘
                       ▼
                DocumentData
                       ▼
                Text Cleaning
                       ▼
                  Chunking
                       ▼
          BGE Embedding Generation
                       ▼
              Qdrant Vector DB
                       ▼
             Semantic Retrieval
                       ▼
             Large Language Model
                       ▼
                 Final Answer
```

---

# ✨ Features Implemented

## Backend Foundation

* FastAPI application
* Modular project architecture
* API routing
* Swagger documentation
* Environment configuration

---

## File Upload

* PDF upload
* PNG upload
* JPG upload
* File type validation
* UUID-based file naming
* Automatic file storage

---

## Document Processing

* Document Processing Pipeline
* File Type Detection
* Pipeline Routing
* Processing Orchestrator

---

## PDF Processing

* PDF Text Extraction
* Multi-page traversal
* Character counting
* Empty document detection
* Text preview generation

---

## OCR Processing

* PaddleOCR Integration
* OCR Service
* Image Text Extraction
* Scanned PDF Support

---

## Text Processing

* Text Cleaning
* Smart Text Chunking
* Overlapping Chunks
* Chunk Metadata

---

## Embedding Generation

* Sentence Transformers
* BAAI/bge-small-en-v1.5
* Normalized Embeddings
* Embedding Data Model

---

## Document Intelligence

* Document Classification
* OCR Decision Engine
* Unified Document Data Model
* Pydantic Schemas

---

## Software Architecture

* Service Layer
* Pipeline Architecture
* Separation of Concerns
* Modular Design
* Clean Code Principles

---

## Containerization

* Dockerfile
* Docker Image
* Containerized FastAPI Application
* Optimized Docker Build Context
* .dockerignore
