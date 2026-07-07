# 📄 Document Intelligence Engine

A production-ready AI Document Intelligence Engine that understands documents using OCR, Retrieval-Augmented Generation (RAG), and Large Language Models.

## 🎯 Project Goal

Build an AI backend capable of:

- Uploading PDF and image documents
- Extracting text using OCR
- Understanding document structure
- Generating embeddings
- Semantic search with a Vector Database
- Answering questions using RAG
- Producing structured JSON from documents
- Summarizing documents

---

## 🛠 Tech Stack

- Python
- FastAPI
- OpenAI API *(planned)*
- Qdrant *(planned)*
- PyMuPDF *(planned)*
- PaddleOCR *(planned)*
- Docker *(planned)*

---

## 📁 Project Structure

```text
document-intelligence-engine/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── pipelines/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── data/
│   └── uploads/
│
├── docs/
├── tests/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

## ✅ Completed Features

- ✔ Project structure initialization
- ✔ FastAPI application setup
- ✔ Interactive Swagger API documentation
- ✔ Root endpoint (`/`)
- ✔ Health check endpoint (`/health`)
- ✔ File upload endpoint (`/upload`)
- ✔ File storage service
- ✔ Automatic creation of the uploads directory
- ✔ Unique filename generation using UUID
- ✔ Support for PDF and image uploads

---

## 🚧 Current Phase

### Phase 1 — FastAPI Foundation ✅

Completed:

- FastAPI project initialization
- API routing
- Health endpoint
- File upload endpoint
- File saving service

### Next Phase

- OCR Pipeline
- Text Extraction
- Document Parsing

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/upload` | Upload a document |

---

## 📌 Roadmap

- [x] Initialize project
- [x] Build FastAPI backend
- [x] Upload API
- [x] File Storage Service
- [ ] OCR Integration
- [ ] Text Cleaning
- [ ] Chunking
- [ ] Embeddings
- [ ] Vector Database
- [ ] Semantic Search
- [ ] RAG Pipeline
- [ ] LLM Integration
- [ ] Docker Deployment

---

## 👨‍💻 Author

**Hesham Elwakeel**

# 📄 Document Intelligence Engine

A production-ready AI Document Intelligence Engine built with FastAPI and modern AI technologies.

The system is designed to understand, process, and retrieve information from documents using OCR, Retrieval-Augmented Generation (RAG), Vector Databases, and Large Language Models.

---

# 🚀 Project Goal

Build a scalable AI backend capable of:

- Uploading PDF and image documents
- Detecting document types automatically
- Extracting text from PDFs
- Performing OCR on scanned documents
- Cleaning and preprocessing extracted text
- Splitting documents into semantic chunks
- Generating embeddings
- Storing embeddings in a Vector Database
- Semantic search
- Retrieval-Augmented Generation (RAG)
- Question Answering over documents
- Document Summarization
- Structured JSON extraction from documents

---

# 🛠 Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn

### AI

- PyMuPDF
- PaddleOCR *(Coming Soon)*
- OpenAI API *(Coming Soon)*

### Vector Database

- Qdrant *(Coming Soon)*

### Future Infrastructure

- Docker
- Docker Compose
- Redis
- PostgreSQL

---

# 📂 Project Structure

```text
document-intelligence-engine/

├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── pipelines/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── data/
│   └── uploads/
│
├── docs/
├── tests/
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# ✅ Features Implemented

## Backend

- FastAPI application
- Modular project architecture
- API routing
- Swagger documentation

---

## File Upload

- Upload PDF documents
- Upload PNG images
- Upload JPG images
- File type validation
- UUID-based file naming
- Automatic file storage

---

## Document Processing

- Document Processing Pipeline
- Document Type Detection
- Pipeline Routing

---

## PDF Processing

- PDF Text Extraction
- Page Traversal
- Character Counting
- Empty Document Detection
- Preview Generation

---

# 🚧 Current Progress

Current Phase

> PDF Text Extraction

Completed Roadmap

- ✅ Project Initialization
- ✅ FastAPI Setup
- ✅ API Routing
- ✅ Upload Endpoint
- ✅ File Validation
- ✅ File Storage Service
- ✅ Document Processing Pipeline
- ✅ Document Type Detection
- ✅ PDF Text Extraction

Upcoming

- OCR Integration
- Image Processing
- Text Cleaning
- Chunking
- Embeddings
- Vector Database
- Semantic Search
- RAG Pipeline
- LLM Integration
- Production Deployment

---

# 🏗 Architecture

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
   ├──────────────┐
   ▼              ▼
PDF Service   Image Service (Coming Soon)
   │
   ▼
Extract Text
```

---

# 📌 Next Milestone

Implement OCR support for scanned PDF documents and images using PaddleOCR.

Future pipeline:

```text
Upload

↓

Save File

↓

Detect File Type

↓

PDF / Image Pipeline

↓

OCR (if needed)

↓

Clean Text

↓

Chunk Text

↓

Embeddings

↓

Qdrant

↓

RAG

↓

LLM

↓

Answer
```

---

# 🎯 Project Vision

This project is being developed as a production-oriented AI Engineering portfolio project.

The goal is not only to build an AI application, but also to follow software engineering best practices including:

- Clean Architecture
- Separation of Concerns
- Service Layer
- Pipeline Architecture
- Modular Design
- Production-ready Code

---

# 👨‍💻 Author

**Hesham Hassan Mohamed Ali**

Data Analyst | AI Engineer

Building production-ready AI systems with Python, FastAPI, Computer Vision, and Large Language Models.

AI Engineer | Data Scientist

---

Built as a production-oriented AI Engineering portfolio project.
