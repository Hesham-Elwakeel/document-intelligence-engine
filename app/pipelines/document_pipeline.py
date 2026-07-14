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
- Return a unified processing result for downstream components.

This class acts as the orchestrator of the document processing workflow,
delegating the actual extraction and OCR tasks to specialized services.
"""

from pathlib import Path
from app.services.pdf_service import extract_text_from_pdf
from app.services.document_classifier import DocumentClassifier
from app.services.ocr_service import OCRService


class DocumentPipeline:

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

        document = extract_text_from_pdf(file_path)

        # print(document.pages)
        # print(document.characters)
        # print(document.is_empty)

        # Take a decision based on the extracted document
        classifier = DocumentClassifier()


        decision = classifier.classify(document)

        if decision == "ocr":

            ocr_service = OCRService()

            ocr_document = ocr_service.extract_text(file_path)

            return {
                "pipeline": "pdf",
                "decision": decision,
                "characters": ocr_document.characters,
                "is_empty": ocr_document.is_empty,
                "ocr_preview": ocr_document.text[:500]
            }

        print(f"Decision: {decision}")

        return {
            "pipeline": "pdf",
            "decision": decision,
            "pages": document.pages,
            "characters": document.characters,
            "is_empty": document.is_empty,
            "preview": document.text[:500]
        }
    


    async def _process_image(self, file_path: Path):

        print("Image pipeline selected")

        return {
            "pipeline": "image",
            "file": str(file_path)
      }
