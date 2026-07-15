#  Document Intelligence Engine

A production-ready AI Document Intelligence Engine built with **FastAPI**, **Computer Vision**, and **Large Language Models**.

The system is designed to understand, process, and retrieve information from documents using OCR, Retrieval-Augmented Generation (RAG), Vector Databases, and modern AI techniques.

---

#  Project Goal

Build a scalable AI backend capable of:

- Uploading PDF and image documents
- Detecting document types automatically
- Extracting text from digital PDFs
- Performing OCR on scanned documents
- Classifying documents before processing
- Cleaning and preprocessing extracted text
- Splitting documents into semantic chunks
- Generating embeddings
- Storing embeddings in a Vector Database
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- Question Answering over documents
- Document Summarization
- Structured JSON extraction

---

#  Tech Stack

## Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

## AI & Document Processing

- PyMuPDF
- PaddleOCR *(Integration in Progress)*
- OpenAI API *(Planned)*

## Vector Database

- Qdrant *(Planned)*

## Infrastructure

- Docker *(Planned)*
- Docker Compose *(Planned)*
- PostgreSQL *(Planned)*
- Redis *(Planned)*

---

#  Project Structure

```text
document-intelligence-engine/

├── app/
│   ├── api/
│   ├── core/
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

#  Features Implemented

## Backend Foundation

- FastAPI application
- Modular project architecture
- API routing
- Swagger documentation
- Environment configuration

---

## File Upload

- PDF upload
- PNG upload
- JPG upload
- File type validation
- UUID-based file naming
- Automatic file storage

---

## Document Processing

- Document Processing Pipeline
- File Type Detection
- Pipeline Routing
- Processing Orchestrator

---

## PDF Processing

- PDF Text Extraction
- Multi-page traversal
- Character counting
- Empty document detection
- Text preview generation

---

## Document Intelligence

- Document Classification
- OCR Decision Engine
- Unified Document Data Model
- Pydantic-based Schemas

---

## Software Architecture

- Service Layer
- Pipeline Architecture
- Separation of Concerns
- Modular Design
- Clean Code Principles

---

#  Current Progress

## Current Phase

> OCR Integration with PaddleOCR

## Completed Milestones

### Milestone 1 — Project Foundation 

- Project Initialization
- FastAPI Setup
- API Routing
- Swagger Documentation

### Milestone 2 — Document Processing Core 

- Upload Endpoint
- File Validation
- File Storage Service
- Document Processing Pipeline
- Document Type Detection
- PDF Text Extraction
- Document Classification
- Unified Document Model (Pydantic)

### Milestone 3 — OCR Integration 

Current Work:

- PaddleOCR Integration
- OCR Service
- Image Processing

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
Validation
   │
   ▼
File Service
   │
   ▼
Document Pipeline
   │
   ├──────────────────────┐
   ▼                      ▼
PDF Pipeline        Image Pipeline
   │                      │
   ▼                      ▼
PDF Service         OCR Service
   │                      │
   ▼                      ▼
Document Classifier        │
   │                       │
   ├───────────────┐       │
   ▼               ▼       ▼
Direct Text      OCR Required
        │              │
        └───────► DocumentData
```

---

#  Roadmap

##  Completed

- FastAPI Backend
- File Upload
- File Storage
- Processing Pipeline
- PDF Extraction
- Document Classification
- Pydantic Models

##  In Progress

- PaddleOCR Integration
- OCR Engine
- Image Processing

##  Upcoming

- Text Cleaning
- Document Chunking
- Embedding Generation
- Qdrant Integration
- Semantic Search
- RAG Pipeline
- LLM Integration
- Docker Deployment

---

#  Project Vision

This project is being developed as a production-oriented AI Engineering portfolio project.

The goal is not only to build an AI application but also to follow modern software engineering practices including:

- Clean Architecture
- SOLID Principles
- Separation of Concerns
- Pipeline-Based Processing
- Service-Oriented Design
- Production-Ready Code

---

# 👨‍💻 Author

**Hesham Elwakeel**

**AI Engineer | Computer Vision Engineer**

Building production-ready AI systems using Python, FastAPI, Computer Vision, Retrieval-Augmented Generation (RAG), and Large Language Models.

· [LinkedIn](https://linkedin.com/in/hesham-elwakeel) · heshamelwakeel17@gmail.com

---
