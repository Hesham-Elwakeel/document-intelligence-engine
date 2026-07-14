import fitz
from pathlib import Path

from app.schemas.document import DocumentData


def extract_text_from_pdf(file_path: Path) -> DocumentData:
    """
    Extract all text from a PDF document.
    """

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    result = DocumentData(
        text=text,
        characters=len(text),
        is_empty=len(text.strip()) == 0,
        pages=len(document),
        source="pdf"
    )

    document.close()

    return result