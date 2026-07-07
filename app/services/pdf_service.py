import fitz
from pathlib import Path


def extract_text_from_pdf(file_path: Path):
    """
    Extract all text from a PDF document.
    """

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    result = {
        "text": text,
        "pages": len(document),
        "characters": len(text),
        "is_empty": len(text.strip()) == 0
    }

    document.close()

    return result
