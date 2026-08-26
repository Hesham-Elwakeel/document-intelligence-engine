Document Intelligence Engine

A production-oriented AI Document Intelligence Engine built with FastAPI, Computer Vision, Vector Databases, and modern AI/NLP techniques.

<p align="center">
<img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/FastAPI-0.138.1-009688?logo=fastapi&logoColor=white" alt="FastAPI">
<img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Qdrant-Vector_DB-DC244C?logo=qdrant&logoColor=white" alt="Qdrant">
<img src="https://img.shields.io/badge/PaddleOCR-OCR-00A5E0?logo=paddlepaddle&logoColor=white" alt="PaddleOCR">
<img src="https://img.shields.io/badge/PyMuPDF-PDF_Processing-000000?logo=adobeacrobatreader&logoColor=white" alt="PyMuPDF">
<img src="https://img.shields.io/badge/Sentence_Transformers-Embeddings-FF6F00" alt="Sentence Transformers">
<img src="https://img.shields.io/badge/HuggingFace-BGE-yellow?logo=huggingface&logoColor=black" alt="HuggingFace">
</p>

<p align="center">
<img src="https://img.shields.io/badge/Status-In_Development-orange" alt="Project Status">
<img src="https://img.shields.io/badge/Architecture-Modular-blue" alt="Architecture">
<img src="https://img.shields.io/badge/Focus-AI_Engineering-purple" alt="AI Engineering">
</p>

The system is designed to ingest, process, understand, and retrieve information from PDF and image documents using OCR, document classification, text cleaning, chunking, vector embeddings, Qdrant, and semantic search.

The project is being developed as a backend-focused AI Engineering portfolio project, with a strong emphasis on modular architecture, separation of concerns, containerization, and production-oriented design.

Project Goal

Build a scalable AI backend capable of:

Uploading PDF and image documents

Validating uploaded files

Detecting document types automatically

Extracting text from digital PDFs

Performing OCR on scanned documents and images

Classifying documents before processing

Cleaning and preprocessing extracted text

Splitting documents into overlapping chunks

Preserving page and source metadata

Generating vector embeddings

Storing embeddings in a Vector Database

Semantic Search

Metadata filtering

Retrieval-Augmented Generation (RAG)

Question Answering over documents

Document Summarization

Structured JSON extraction

Tech Stack

Backend

Python

FastAPI

Uvicorn

Pydantic

AI & Document Processing

PyMuPDF

PaddleOCR

Sentence Transformers

BAAI/bge-small-en-v1.5

OpenAI API (Planned)

Vector Database

Qdrant

qdrant-client

Infrastructure

Docker

Docker Compose

PostgreSQL (Planned)

Redis (Planned)

Project Structure

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
│   ├── search_service.py
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

Document Processing Workflow

The current ingestion pipeline follows this flow:

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

Features Implemented

Backend Foundation

FastAPI application

Modular project architecture

API routing

Swagger / OpenAPI documentation

Pydantic schemas

Service-based architecture

Pipeline-based document processing

File Upload

PDF upload

PNG upload

JPG upload

JPEG upload

File type validation

UUID-based file naming

Automatic file storage

Document Processing

Document Processing Pipeline

File Type Detection

Pipeline Routing

Processing Orchestrator

Unified Document Data Model

Page-level document metadata

PDF Processing

PDF text extraction using PyMuPDF

Multi-page traversal

Page boundary preservation

Character counting

Empty document detection

Text preview generation

Source filename preservation

OCR Processing

PaddleOCR integration

OCR Service

Image text extraction

Scanned PDF processing

OCR decision engine

Page-level OCR text extraction

The system determines whether a PDF already contains extractable text or requires OCR.

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

Text Processing

Text cleaning

Overlapping chunking

Configurable chunk size

Configurable overlap

Page metadata preservation

Source metadata preservation

Current chunking configuration:

Chunk Size: 500 characters
Overlap:    100 characters

Embedding Generation

Sentence Transformers

BAAI/bge-small-en-v1.5

384-dimensional embeddings

Normalized embeddings

Query embedding generation

Embedding data model

Current embedding flow:

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

Qdrant Vector Storage

Qdrant has been integrated into the document processing pipeline.

The system creates a Qdrant collection named:

documents

with:

Vector Size: 384
Distance: Cosine

Each document chunk is stored as a Qdrant Point containing:

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

Qdrant Service

The project includes:

app/services/qdrant_service.py

The service currently provides:

Collection creation

Embedding storage

Vector configuration

Payload management

Vector similarity search

Score threshold filtering

Qdrant client initialization

Semantic Search

Semantic Search has now been implemented on top of the Qdrant vector database.

The search pipeline follows:

User Query
    │
    ▼
Query Embedding
    │
    ▼
Qdrant Similarity Search
    │
    ▼
Score Filtering
    │
    ▼
Top-K Relevant Chunks
    │
    ▼
Clean Search Response

Search API

The search endpoint is:

POST /search

Example request:

{
  "query": "What experience does Hesham have with Power BI?",
  "limit": 5,
  "min_score": 0.65
}

Search Parameters

Parameter

Type

Description

query

string

User's semantic search query

limit

integer

Maximum number of results

min_score

float | null

Minimum similarity score required

min_score is optional. When provided, Qdrant filters out results whose similarity score is below the threshold.

Example:

min_score = 0.65

Results with:

score < 0.65

are excluded.

Search Response

The API returns a clean response containing:

{
  "query": "What experience does Hesham have with Power BI?",
  "results": [
    {
      "score": 0.6911489,
      "text": "...",
      "chunk_index": 0,
      "page": 1,
      "source": "document.pdf"
    }
  ],
  "min_score": 0.65
}

The search implementation separates responsibilities between:

Search API
    │
    ▼
SearchService
    │
    ├── EmbeddingService
    │
    └── QdrantService

This keeps the API layer independent from the vector database implementation.

Metadata

Document metadata is preserved throughout the processing pipeline.

Current metadata includes:

page
source
chunk_index

The metadata is attached to each chunk before embedding and is stored inside the Qdrant payload.

Current flow:

PDF / Image
    │
    ▼
PageData
    │
    ▼
ChunkData
    │
    ├── text
    ├── page
    └── source
    │
    ▼
EmbeddingData
    │
    ├── embedding
    ├── chunk_index
    ├── page
    └── source
    │
    ▼
Qdrant Payload

Metadata filtering is the next retrieval improvement.

Docker

The application is containerized using Docker.

The Docker image is based on:

python:3.13-slim

The Docker configuration includes system dependencies required by the document processing and OCR stack.

The project also uses a .dockerignore file to prevent unnecessary files such as the local virtual environment from being sent to the Docker build context.

Docker Compose

The project uses Docker Compose to run the application and Qdrant together.

Current architecture:

Docker Compose
│
├── API
│   └── FastAPI
│
└── Qdrant
    └── Vector Database

The API communicates with Qdrant through the Docker network using:

QDRANT_URL=http://qdrant:6333

Qdrant data is persisted using a Docker volume:

qdrant_data

This allows vector data to survive container recreation.

Current Architecture

                         Client
                           │
                           ▼
                     FastAPI API
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       Upload Endpoint            Search Endpoint
              │                         │
              ▼                         ▼
         File Service              SearchService
              │                    │           │
              ▼                    ▼           ▼
      Document Pipeline      EmbeddingService QdrantService
              │                         │           │
              │                         └─────┬─────┘
              │                               │
              ▼                               ▼
       PDF / Image Processing              Qdrant
              │                               │
              ▼                               ▼
        Text Cleaning                  Vector Search
              │                               │
              ▼                               ▼
          Chunking                    Search Results
              │
              ▼
        Embedding Service
              │
              ▼
        Qdrant Service
              │
              ▼
           Qdrant

Software Architecture

The project follows a modular service-oriented architecture.

API Layer

Responsible for:

HTTP requests

File uploads

Search requests

API routing

Request/response handling

Pipeline Layer

Responsible for:

Orchestrating document processing

Routing documents

Coordinating multiple services

Service Layer

Responsible for specialized operations:

FileService
PDFService
OCRService
DocumentClassifier
TextCleaner
ChunkService
EmbeddingService
QdrantService
SearchService

Schema Layer

Responsible for structured data models using Pydantic.

Examples:

DocumentData
PageData
ChunkData
EmbeddingData
SearchRequest
SearchResult
SearchResponse
PipelineData

This architecture follows:

Separation of Concerns

Single Responsibility

Modular Design

Service-Oriented Design

Pipeline-Based Processing

Clean Code Principles

Current Progress

Current Phase

Semantic Search & Retrieval — In Progress

The project has successfully completed the document ingestion, embedding, and vector storage phases.

Current pipeline:

Upload
  ↓
Document Processing
  ↓
OCR / PDF Extraction
  ↓
Text Cleaning
  ↓
Page Preservation
  ↓
Chunking
  ↓
Embeddings
  ↓
Qdrant Vector Storage
  ↓
Semantic Search
  ↓
Score Threshold Filtering

Completed Milestones

Milestone 1 — Project Foundation

Project Initialization

FastAPI Setup

API Routing

Swagger Documentation

Modular Architecture

Milestone 2 — Document Processing Core

Upload Endpoint

File Validation

File Storage Service

Document Processing Pipeline

Document Type Detection

PDF Text Extraction

Document Classification

Unified Document Model

Milestone 3 — OCR Integration

PaddleOCR Integration

OCR Service

Image Processing

Scanned PDF Processing

OCR Decision Engine

Page-level OCR extraction

Milestone 4 — Text Processing & Embeddings

Text Cleaning

Chunking Service

Overlapping Chunks

Page metadata

Source metadata

Embedding Service

Sentence Transformers Integration

BAAI/bge-small-en-v1.5 Integration

384-dimensional normalized embeddings

Query embedding generation

Milestone 5 — Docker & Containerization

Dockerfile

Docker Image

Docker Build Optimization

.dockerignore

Docker Container Execution

Docker Compose

API Container

Qdrant Container

Docker Networking

Persistent Qdrant Volume

Milestone 6 — Qdrant Integration

qdrant-client integration

Qdrant Service

Qdrant Collection Creation

Vector Configuration

Cosine Similarity

Point Creation

Vector Storage

Payload Storage

API → Qdrant communication

Persistent Vector Database

Milestone 7 — Semantic Search

Search Request schema

Search Result schema

Search Response schema

Search API endpoint

Query embedding

Qdrant similarity search

Top-K retrieval

Similarity score

min_score threshold

Clean JSON response

Separation between Search API and Qdrant

Page/source metadata in search results

Example:

User Query
    ↓
SearchRequest
    ↓
SearchService
    ↓
EmbeddingService
    ↓
QdrantService
    ↓
Qdrant
    ↓
Filtered Results
    ↓
SearchResponse

Current Status

The document ingestion and semantic search foundation are now implemented.

The system can currently:

Upload
   ↓
Extract / OCR
   ↓
Clean
   ↓
Preserve Page Metadata
   ↓
Chunk
   ↓
Embed
   ↓
Store in Qdrant
   ↓
Generate Query Embedding
   ↓
Semantic Search
   ↓
Apply Score Threshold
   ↓
Return Relevant Chunks

The next step is to improve retrieval quality with metadata filtering.

Roadmap

Completed

FastAPI Backend

File Upload

File Validation

File Storage

PDF Extraction

OCR Integration

Document Classification

Text Cleaning

Page-level text preservation

Document Chunking

Embedding Generation

Docker

Docker Compose

Qdrant Integration

Vector Storage

Persistent Qdrant Storage

Semantic Search

Top-K Retrieval

Score Threshold Filtering

Next Step

Metadata Filtering

Implement filtering during semantic search using document metadata such as:

source
page

Example use cases:

Search only inside a specific document

or:

Search only inside a specific page

Target workflow:

User Query
      │
      ├── Metadata Filters
      │
      ▼
Question Embedding
      │
      ▼
Qdrant Similarity Search
      │
      ▼
Score Threshold
      │
      ▼
Top-K Relevant Chunks

Upcoming

Retrieval Quality Improvements

Metadata filtering

Better top-K strategy

Duplicate / overlapping chunk handling

Retrieval quality evaluation

Chunking improvements

Retriever abstraction

Context selection

RAG

Retrieval-Augmented Generation pipeline

Context construction

Context assembly

Prompt construction

LLM integration

LLM

OpenAI API

Question Answering

Context-aware responses

Document Intelligence

Document Summarization

Structured JSON Extraction

Advanced document understanding

Infrastructure

PostgreSQL

Redis

Docker Compose improvements

Production deployment

Project Vision

This project is being developed as a production-oriented AI Engineering portfolio project.

The goal is not only to build an AI application, but also to apply modern software engineering and AI system design principles.

The project focuses on:

Clean Architecture

SOLID Principles

Separation of Concerns

Service-Oriented Design

Pipeline-Based Processing

Vector Search

Retrieval-Augmented Generation

Containerization

Production-oriented backend engineering

Retrieval quality and evaluation

The final goal is to build an end-to-end document intelligence system capable of understanding documents and answering questions using retrieved document context.

Author

Hesham Elwakeel

AI Engineer | Computer Vision Engineer | Data Scientist

Building production-oriented AI systems using Python, FastAPI, Computer Vision, Vector Databases, Retrieval-Augmented Generation (RAG), and Large Language Models.

LinkedIn: https://linkedin.com/in/hesham-elwakeel

Email: heshamelwakeel17@gmail.com

Current Status

Document ingestion, vector storage, and semantic search foundation completed.

The project currently implements:

Upload → PDF/OCR Processing → Cleaning → Page Metadata → Chunking → Embeddings → Qdrant Vector Storage → Semantic Search → Score Threshold Filtering

The project is now entering the Metadata Filtering and Retrieval Quality phase, which will serve as the foundation for the upcoming RAG pipeline.
