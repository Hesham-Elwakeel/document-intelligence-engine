from pathlib import Path
from paddleocr import PaddleOCR
from app.schemas.document import DocumentData

"""class OCRService:
    
    A service class  Responsible for extracting text from scanned documents
    
    def extract_text(self, file_path: Path):

        print(f"Running OCR on file: {file_path}")

        return "OCR Processing will be implemented later"
    """

class OCRService:

    def __init__(self):

        self.ocr = PaddleOCR(
            use_doc_orientation_classify=False, #do not detect page orientation.
            use_doc_unwarping=False, #do not correct warped or curved documents.
            use_textline_orientation=False, #do not detect text line orientation.
            lang="en"
        )

    def extract_text(self, file_path: Path) -> dict:

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
    #Convert PaddleOCR output into plain text.

        lines = []

        for page in result:

            if hasattr(page, "rec_texts"):

                lines.extend(page.rec_texts)

        return "\n".join(lines)     