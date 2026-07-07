
from pathlib import Path
from app.services.pdf_service import extract_text_from_pdf

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

        pdf_data = extract_text_from_pdf(file_path)

        print(f"pages: {pdf_data['pages']}")
        print(f"characters: {pdf_data['characters']}")
        print(f"is_empty: {pdf_data['is_empty']}")

        return {
            "pipeline": "pdf",
            "pages": pdf_data["pages"],
            "characters": pdf_data["characters"],
            "is_empty": pdf_data["is_empty"],
            "preview": pdf_data["text"][:500]
        }

    async def _process_image(self, file_path: Path):

        print("Image pipeline selected")

        return {
            "pipeline": "image",
            "file": str(file_path)
            
        }
    
