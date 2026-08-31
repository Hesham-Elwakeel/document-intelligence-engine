#  Document Intelligence Engine

A production-oriented AI Document Intelligence Engine built with **FastAPI**, **Computer Vision**, **Vector Databases**, and modern **AI/NLP techniques**.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/FastAPI-0.138.1-009688?logo=fastapi&logoColor=white" alt="FastAPI"> <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white" alt="Docker"> <img src="https://img.shields.io/badge/Qdrant-Vector_DB-DC244C?logo=qdrant&logoColor=white" alt="Qdrant"> <img src="https://img.shields.io/badge/PaddleOCR-OCR-00A5E0?logo=paddlepaddle&logoColor=white" alt="PaddleOCR"> <img src="https://img.shields.io/badge/PyMuPDF-PDF_Processing-000000?logo=adobeacrobatreader&logoColor=white" alt="PyMuPDF"> <img src="https://img.shields.io/badge/Sentence_Transformers-Embeddings-FF6F00" alt="Sentence Transformers"> <img src="https://img.shields.io/badge/HuggingFace-BGE-yellow?logo=huggingface&logoColor=black" alt="HuggingFace"> </p>

<p align="center"> <img src="https://img.shields.io/badge/Status-In_Development-orange" alt="Project Status"> <img src="https://img.shields.io/badge/Architecture-Modular-blue" alt="Architecture"> <img src="https://img.shields.io/badge/Focus-AI_Engineering-purple" alt="AI Engineering"> </p>

The system is designed to ingest, process, understand, and retrieve information from PDF and image documents using OCR, document classification, semantic chunking, vector embeddings, and Qdrant.

The project is being developed as a backend-focused **AI Engineering portfolio project**, with a strong emphasis on modular architecture, separation of concerns, containerization, and production-oriented design.

---


#  Project Goal

Build a scalable AI backend capable of:

* Uploading PDF and image documents
* Validating uploaded files
* Detecting document types automatically
* Extracting text from digital PDFs
* Performing OCR on scanned documents and images
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

* Qdrant
* qdrant-client

## Infrastructure

* Docker
* Docker Compose
* PostgreSQL *(Planned)*
* Redis *(Planned)*

---

#  Project Structure

```text
document-intelligence-engine/

├── app/
│
├── api/
│
├── core/
│
├── pipelines/
│   └── document_pipeline.py
│
├── schemas/
│   ├── chunk.py
│   ├── document.py
│   ├── embedding.py
│   └── pipeline.py
│
├── services/
│   ├── chunking_service.py
│   ├── document_classifier.py
│   ├── embedding_service.py
│   ├── file_service.py
│   ├── ocr_service.py
│   ├── pdf_service.py
│   ├── qdrant_service.py
│   └── text_cleaner.py
│
├── utils/
│
└── main.py

├── data/
│   └── uploads/

├── docs/

├── tests/

├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── README.md
└── .env.example
```

---

#  Document Processing Workflow

The current ingestion pipeline follows this flow:

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
PDF Text Extraction      PaddleOCR
        │                      │
        ▼                      │
Document Classification        │
        │                      │
   ┌────┴────┐                 │
   ▼         ▼                 │
  Text       OCR               │
   │         │                 │
   └────┬────┘─────────────────┘
        ▼
   Text Cleaning
        │
        ▼
      Chunking
        │
        ▼
BGE Embedding Generation
        │
        ▼
      Qdrant
        │
        ▼
  Vector Storage
```

---

# ✅ Features Implemented

## Backend Foundation

* FastAPI application
* Modular project architecture
* API routing
* Swagger / OpenAPI documentation
* Pydantic schemas
* Service-based architecture
* Pipeline-based document processing

---

##  File Upload

* PDF upload
* PNG upload
* JPG upload
* JPEG upload
* File type validation
* UUID-based file naming
* Automatic file storage

---

##  Document Processing

* Document Processing Pipeline
* File Type Detection
* Pipeline Routing
* Processing Orchestrator
* Unified Document Data Model

---

##  PDF Processing

* PDF text extraction using PyMuPDF
* Multi-page traversal
* Character counting
* Empty document detection
* Text preview generation

---

##  OCR Processing

* PaddleOCR integration
* OCR Service
* Image text extraction
* Scanned PDF processing
* OCR decision engine

The system determines whether a PDF already contains extractable text or requires OCR.

```text
PDF
 │
 ▼
Extract Text
 │
 ▼
Classify Document
 │
 ├── Text Available ──► Continue
 │
 └── OCR Required ────► PaddleOCR
```

---

##  Text Processing

* Text cleaning
* Smart text chunking
* Overlapping chunks
* Chunk metadata

---

##  Embedding Generation

* Sentence Transformers
* BAAI/bge-small-en-v1.5
* 384-dimensional embeddings
* Normalized embeddings
* Embedding data model

Current embedding flow:

```text
Document
    │
    ▼
Text Chunks
    │
    ▼
BGE-small-en-v1.5
    │
    ▼
384-dimensional Vectors
```

---

#  Qdrant Vector Storage

Qdrant has now been integrated into the document processing pipeline.

The system creates a Qdrant collection named:

```text
documents
```

with:

```text
Vector Size: 384
Distance: Cosine
```

Each document chunk is stored as a Qdrant Point containing:

```text
Point
│
├── ID
│
├── Vector
│   └── 384 dimensions
│
└── Payload
    ├── text
    ├── chunk_index
    ├── page
    └── source
```

### Qdrant Service

The project includes:

```text
app/services/qdrant_service.py
```

The service currently provides:

* Collection creation
* Embedding storage
* Vector configuration
* Payload management
* Qdrant client initialization

---

# 🐳 Docker

The application is containerized using Docker.

The Docker image is based on:

```text
python:3.13-slim
```

The Docker configuration includes system dependencies required by the document processing and OCR stack.

The project also uses a `.dockerignore` file to prevent unnecessary files such as the local virtual environment from being sent to the Docker build context.

---

# 🐳 Docker Compose

The project uses Docker Compose to run the application and Qdrant together.

Current architecture:

```text
Docker Compose
│
├── API
│   └── FastAPI
│
└── Qdrant
    └── Vector Database
```

The API communicates with Qdrant through the Docker network using:

```text
QDRANT_URL=http://qdrant:6333
```

Qdrant data is persisted using a Docker volume:

```text
qdrant_data
```

This allows vector data to survive container recreation.

---

#  Current Architecture

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
                     File Service
                           │
                           ▼
                  Document Pipeline
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
        PDF Pipeline              Image Pipeline
              │                         │
              ▼                         ▼
       PDF Extraction               OCR Service
              │                         │
              ▼                         │
      Document Classifier              │
              │                         │
         ┌────┴────┐                    │
         ▼         ▼                    │
        Text       OCR                  │
         │         │                    │
         └────┬────┘────────────────────┘
              ▼
        Text Cleaner
              │
              ▼
        Chunk Service
              │
              ▼
      Embedding Service
              │
              ▼
        Qdrant Service
              │
              ▼
           Qdrant
              │
              ▼
      Vector Storage
```

---

#  Software Architecture

The project follows a modular service-oriented architecture.

### API Layer

Responsible for:

* HTTP requests
* File uploads
* API routing
* Request/response handling

### Pipeline Layer

Responsible for:

* Orchestrating document processing
* Routing documents
* Coordinating multiple services

### Service Layer

Responsible for specialized operations:

```text
FileService
PDFService
OCRService
DocumentClassifier
TextCleaner
ChunkService
EmbeddingService
QdrantService
```

### Schema Layer

Responsible for structured data models using Pydantic.

Examples:

```text
DocumentData
ChunkData
EmbeddingData
PipelineData
```

This architecture follows:

* Separation of Concerns
* Single Responsibility
* Modular Design
* Service-Oriented Design
* Pipeline-Based Processing
* Clean Code Principles

---

#  Current Progress

## Current Phase

> **Vector Database Integration — Completed**

The project has successfully reached the end of the document ingestion and vector storage phase.

Current pipeline:

```text
Upload
  ↓
Document Processing
  ↓
OCR / PDF Extraction
  ↓
Text Cleaning
  ↓
Chunking
  ↓
Embeddings
  ↓
Qdrant Vector Storage
```

---

#  Completed Milestones

## Milestone 1 — Project Foundation

* Project Initialization
* FastAPI Setup
* API Routing
* Swagger Documentation
* Modular Architecture

---

## Milestone 2 — Document Processing Core

* Upload Endpoint
* File Validation
* File Storage Service
* Document Processing Pipeline
* Document Type Detection
* PDF Text Extraction
* Document Classification
* Unified Document Model

---

## Milestone 3 — OCR Integration

* PaddleOCR Integration
* OCR Service
* Image Processing
* Scanned PDF Processing
* OCR Decision Engine

---

## Milestone 4 — Text Processing & Embeddings

* Text Cleaning
* Chunking Service
* Overlapping Chunks
* Embedding Service
* Sentence Transformers Integration
* BAAI/bge-small-en-v1.5 Integration
* 384-dimensional normalized embeddings

---

## Milestone 5 — Docker & Containerization

* Dockerfile
* Docker Image
* Docker Build Optimization
* `.dockerignore`
* Docker Container Execution
* Docker Compose
* API Container
* Qdrant Container
* Docker Networking
* Persistent Qdrant Volume

---

## Milestone 6 — Qdrant Integration

* qdrant-client integration
* Qdrant Service
* Qdrant Collection Creation
* Vector Configuration
* Cosine Similarity
* Point Creation
* Vector Storage
* Payload Storage
* API → Qdrant communication
* Persistent Vector Database

The current system has successfully stored document embeddings in Qdrant.

Example:

```text
Document
   ↓
14 Chunks
   ↓
14 Embeddings
   ↓
14 Qdrant Points
```

---

#  Current Status

The document ingestion pipeline is complete.

The system can currently:

```text
Upload
   ↓
Extract / OCR
   ↓
Clean
   ↓
Chunk
   ↓
Embed
   ↓
Store in Qdrant
```

The next major step is **Semantic Search**.

---

#  Roadmap

##  Completed

* FastAPI Backend
* File Upload
* File Validation
* File Storage
* PDF Extraction
* OCR Integration
* Document Classification
* Text Cleaning
* Document Chunking
* Embedding Generation
* Docker
* Docker Compose
* Qdrant Integration
* Vector Storage
* Persistent Qdrant Storage

---

##  Next Step

### Semantic Search

Implement:

* Query embedding
* Qdrant similarity search
* Cosine similarity
* Top-K retrieval
* Relevant chunk retrieval
* Search service

Target workflow:

```text
User Question
      │
      ▼
Question Embedding
      │
      ▼
Qdrant Similarity Search
      │
      ▼
Top-K Relevant Chunks
```

---

##  Upcoming

### Retrieval

* Retriever component
* Search abstraction
* Metadata filtering
* Context selection

### RAG

* Retrieval-Augmented Generation pipeline
* Context construction
* Prompt construction
* LLM integration

### LLM

* OpenAI API
* Question Answering
* Context-aware responses

### Document Intelligence

* Document Summarization
* Structured JSON Extraction
* Advanced document understanding

### Infrastructure

* PostgreSQL
* Redis
* Docker Compose improvements
* Production deployment

---

# 🎯 Project Vision

This project is being developed as a **production-oriented AI Engineering portfolio project**.

The goal is not only to build an AI application, but also to apply modern software engineering and AI system design principles.

The project focuses on:

* Clean Architecture
* SOLID Principles
* Separation of Concerns
* Service-Oriented Design
* Pipeline-Based Processing
* Vector Search
* Retrieval-Augmented Generation
* Containerization
* Production-oriented backend engineering

The final goal is to build an end-to-end document intelligence system capable of understanding documents and answering questions using retrieved document context.

---

#  Author

**Hesham Elwakeel**

**AI Engineer | Computer Vision Engineer | Data Scientist**

Building production-oriented AI systems using Python, FastAPI, Computer Vision, Vector Databases, Retrieval-Augmented Generation (RAG), and Large Language Models.

* LinkedIn: https://linkedin.com/in/hesham-elwakeel * Email: [heshamelwakeel17@gmail.com](mailto:heshamelwakeel17@gmail.com)

---

#  Current Status

> **Document ingestion and vector storage pipeline completed.**

The system currently implements:

**Upload → PDF/OCR Processing → Cleaning → Chunking → Embeddings → Qdrant Vector Storage**

The project is now entering the **Semantic Search and Retrieval phase**, which will serve as the foundation for the upcoming RAG pipeline.





