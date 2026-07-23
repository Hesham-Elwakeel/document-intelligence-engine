from app.schemas.chunk import ChunkData


class ChunkService:
    """
    Split long text into smaller overlapping chunks.
    """

    def split(
        self,
        text: str,
        chunk_size: int = 500,
        overlap: int = 100
    ) -> list[ChunkData]:

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append(
                ChunkData(
                    id=len(chunks),
                    text=chunk_text
                )
            )

            start += chunk_size - overlap

        return chunks