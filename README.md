#  Document Intelligence Engine

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.138-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![PaddleOCR](https://img.shields.io/badge/OCR-PaddleOCR-00A67E)](https://github.com/PaddlePaddle/PaddleOCR)
[![Sentence Transformers](https://img.shields.io/badge/Embeddings-SentenceTransformers-FF6F00)](https://www.sbert.net/)
[![Qdrant](https://img.shields.io/badge/VectorDB-Qdrant-In%20Progress-DC244C)](https://qdrant.tech/)

A production-ready AI Document Intelligence Engine built with **FastAPI**, **Computer Vision**, **Large Language Models (LLMs)**, and **Vector Databases**.

The system is designed to understand, process, index, retrieve, and reason over documents using OCR, semantic embeddings, Retrieval-Augmented Generation (RAG), and modern AI engineering practices.

---

#  Project Goal

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

#  Tech Stack

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

* Docker 
* Docker Compose *(Planned)*
* PostgreSQL *(Planned)*
* Redis *(Planned)*

---

#  Project Structure

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

#  Processing Workflow

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

#  Features Implemented

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

---

#  Current Progress

## Current Phase

> **Vector Database Integration (Qdrant)**

---

## Completed Milestones

### Milestone 1 — Project Foundation

* Project Initialization
* FastAPI Setup
* API Routing
* Swagger Documentation

---

### Milestone 2 — Document Processing Core

* Upload Endpoint
* File Validation
* File Storage Service
* Document Processing Pipeline
* Document Type Detection
* PDF Text Extraction
* Document Classification
* Unified Document Model (Pydantic)

---

### Milestone 3 — OCR Integration

* PaddleOCR Integration
* OCR Service
* Image Processing
* Scanned PDF Processing

---

### Milestone 4 — Text Processing & Embeddings

* Text Cleaning
* Chunking Service
* Overlapping Chunks
* Embedding Service
* Sentence Transformers Integration
* BAAI/bge-small-en-v1.5 Integration

---

### Milestone 5 — Docker Containerization

* Dockerfile
* Docker Image
* Containerized FastAPI Application
* Optimized Docker Build Context
* `.dockerignore`

---

# Current Architecture

```text
Client
   │
   ▼
FastAPI API
   │
   ▼
Upload Endpoint
   │
   ▼
Validation
   │
   ▼
File Service
   │
   ▼
Document Pipeline
   │
   ├────────────────────────────┐
   ▼                            ▼
PDF Pipeline              Image Pipeline
   │                            │
   ▼                            ▼
PDF Service               OCR Service
   │                            │
   ├──────────────┐             │
   ▼              ▼             ▼
Direct Text    OCR Required
        │             │
        └─────────────┘
               ▼
         DocumentData
               ▼
         Text Cleaner
               ▼
      Chunking Service
               ▼
     Embedding Service
               ▼
        EmbeddingData
               ▼
      Qdrant (Next Step)
```

---

#  Roadmap

##  Completed

* FastAPI Backend
* File Upload
* File Storage
* PDF Extraction
* OCR Integration
* Document Classification
* Text Cleaning
* Document Chunking
* Embedding Generation
* Docker Containerization
* Pydantic Models

---

##  In Progress

* Qdrant Integration
* Vector Storage
* Collection Management

---

## Upcoming

* Semantic Search
* Retriever
* RAG Pipeline
* OpenAI Integration
* Question Answering
* Document Summarization
* Structured JSON Extraction
* Docker Compose
* PostgreSQL
* Redis

---

# 🚀 Quick Start

## Clone Repository

```bash
git clone https://github.com/Hesham-Elwakeel/document-intelligence-engine.git

cd document-intelligence-engine
```

---

## Build Docker Image

```bash
docker build -t document-intelligence-engine .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 --name document-engine document-intelligence-engine
```

---

## API Documentation

After starting the container, open:

```text
http://localhost:8000/docs
```

---

# Project Vision

This project is being developed as a **production-oriented AI Engineering portfolio project**.

The objective is not only to build an AI application but also to follow modern software engineering and MLOps practices, including:

* Clean Architecture
* SOLID Principles
* Separation of Concerns
* Pipeline-Based Processing
* Service-Oriented Design
* Docker Containerization
* Modular AI Components
* Production-Ready Code

The final system will support a complete Retrieval-Augmented Generation (RAG) workflow, enabling intelligent question answering over enterprise documents.

---

# Author

**Hesham Elwakeel**

**AI Engineer | Computer Vision Engineer | Data Scientist**

Building production-ready AI systems 

**LinkedIn** https://linkedin.com/in/hesham-elwakeel **Email** [heshamelwakeel17@gmail.com](mailto:heshamelwakeel17@gmail.com)




