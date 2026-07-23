"""
Document Pipeline

This module is the main entry point for document processing in the
Document Intelligence Engine.

Responsibilities:
- Detect the uploaded file type (PDF or image).
- Route the document to the appropriate processing pipeline.
- Extract text directly from text-based PDFs.
- Classify PDFs to determine whether OCR is required.
- Run OCR for scanned PDFs when necessary.
- Clean extracted text.
- Return a unified processing result for downstream components.

This class acts as the orchestrator of the document processing workflow,
delegating the actual extraction and OCR tasks to specialized services.
"""

from pathlib import Path

from app.services.pdf_service import extract_text_from_pdf
from app.services.document_classifier import DocumentClassifier
from app.services.ocr_service import OCRService
from app.services.text_cleaner import TextCleaner
from app.services.chunking_service import ChunkService
from app.services.embedding_service import EmbeddingService


class DocumentPipeline:
    """
    Main orchestrator responsible for routing documents through the
    appropriate processing pipeline.
    """

    def __init__(self):
        self.cleaner = TextCleaner()
        self.classifier = DocumentClassifier()
        self.ocr_service = OCRService()
        self.chunk_service = ChunkService()
        self.embedding_service = EmbeddingService()

    async def process(self, file_path: Path):

        print(f"Processing file: {file_path}")

        extension = file_path.suffix.lower()

        print(f"Detected file type: {extension}")

        if extension == ".pdf":
            return await self._process_pdf(file_path)

        elif extension in [".png", ".jpg", ".jpeg"]:
            return await self._process_image(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

    async def _process_pdf(self, file_path: Path):

        print("PDF pipeline selected")

        # -------------------------------------------------------------
        # Extract text directly from PDF
        # -------------------------------------------------------------
        document = extract_text_from_pdf(file_path)

        # -------------------------------------------------------------
        # Clean extracted text
        # -------------------------------------------------------------
        document.text = self.cleaner.clean(document.text)
        document.characters = len(document.text)
        document.is_empty = len(document.text.strip()) == 0

        # -------------------------------------------------------------
        # Decide whether OCR is required
        # -------------------------------------------------------------
        decision = self.classifier.classify(document)

        # -------------------------------------------------------------
        # OCR Pipeline
        # -------------------------------------------------------------
        if decision == "ocr":

            document = self.ocr_service.extract_text(file_path)

            document.text = self.cleaner.clean(document.text)
            document.characters = len(document.text)
            document.is_empty = len(document.text.strip()) == 0

        # -------------------------------------------------------------
        # Split document into chunks
        # -------------------------------------------------------------
        chunks = self.chunk_service.split(document.text)

        # -------------------------------------------------------------
        # Generate embeddings
        # -------------------------------------------------------------
        embeddings = self.embedding_service.encode(chunks)

        # -------------------------------------------------------------
        # Final response
        # -------------------------------------------------------------
        return {
            "pipeline": "pdf",
            "decision": decision,
            "pages": document.pages,
            "characters": document.characters,
            "is_empty": document.is_empty,
            "preview": document.text[:500],
            "chunks": len(chunks),
            "embeddings": len(embeddings),
        }

    async def _process_image(self, file_path: Path):

        print("Image pipeline selected")

        # -------------------------------------------------------------
        # OCR Extraction
        # -------------------------------------------------------------
        document = self.ocr_service.extract_text(file_path)

        # -------------------------------------------------------------
        # Clean OCR text
        # -------------------------------------------------------------
        document.text = self.cleaner.clean(document.text)
        document.characters = len(document.text)
        document.is_empty = len(document.text.strip()) == 0

        # -------------------------------------------------------------
        # Split into chunks
        # -------------------------------------------------------------
        chunks = self.chunk_service.split(document.text)

        # -------------------------------------------------------------
        # Generate embeddings
        # -------------------------------------------------------------
        embeddings = self.embedding_service.encode(chunks)

        return {
            "pipeline": "image",
            "characters": document.characters,
            "is_empty": document.is_empty,
            "preview": document.text[:500],
            "chunks": len(chunks),
            "embeddings": len(embeddings),
        }