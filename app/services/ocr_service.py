from pathlib import Path

from paddleocr import PaddleOCR

from app.schemas.document import DocumentData

from app.services.text_cleaner import TextCleaner

class OCRService:
    """
    Service responsible for extracting text from scanned documents
    using PaddleOCR.
    """

    def __init__(self):

        self.ocr = PaddleOCR(
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
            lang="en"
        )

    def extract_text(self, file_path: Path) -> DocumentData:
        """
        run OCR on an image or scanned PDF and return the extracted text
        """

        print(f"Running OCR on: {file_path}")

        result = self.ocr.predict(str(file_path))

        text = self._extract_plain_text(result)

        return DocumentData(
            text=text,
            characters=len(text),
            is_empty=len(text.strip()) == 0,
            source="ocr"
        )

    def _extract_plain_text(self, result) -> str:
        """
        Convert PaddleOCR output into plain text.
        """

        lines = []

        for page in result:

            if isinstance(page, dict):
                lines.extend(page.get("rec_texts", []))

        return "\n".join(lines)