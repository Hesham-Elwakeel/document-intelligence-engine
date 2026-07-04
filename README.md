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

AI Engineer | Data Scientist

---

Built as a production-oriented AI Engineering portfolio project.
