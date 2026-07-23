from sentence_transformers import SentenceTransformer

from app.schemas.chunk import ChunkData
from app.schemas.embedding import EmbeddingData


class EmbeddingService:
    """
    Service responsible for converting text chunks into vector embeddings.
    """

    def __init__(self):
        # load the embedding model
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def encode(self, chunks: list[ChunkData]) -> list[EmbeddingData]:
        """
        Generate embeddings for a list of document chunks.
        """

        # extract only the text from each chunk
        texts = [chunk.text for chunk in chunks]

        # generate embeddings
        vectors = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        embeddings = []

        # pair each chunk with its embedding
        for chunk, vector in zip(chunks, vectors):

            embeddings.append(
                EmbeddingData(
                    text=chunk.text,
                    embedding=vector.tolist(),
                    chunk_index=chunk.id
                )
            )

        return embeddings