from uuid import uuid4
import os

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from app.schemas.embedding import EmbeddingData


class QdrantService:
    """
    Service responsible for storing and retrieving
    document embeddings using Qdrant.
    """

    COLLECTION_NAME = "documents"
    VECTOR_SIZE = 384

    def __init__(self):
        """
        Initialize Qdrant client.
        """

        url = os.getenv(
            "QDRANT_URL",
            "http://localhost:6333"
        )

        self.client = QdrantClient(url=url)

    def create_collection(self) -> None:
        """
        Create the documents collection if it does not exist.
        """

        if not self.client.collection_exists(
            collection_name=self.COLLECTION_NAME
        ):
            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=self.VECTOR_SIZE,
                    distance=Distance.COSINE,
                ),
            )

    def store_embeddings(
        self,
        embeddings: list[EmbeddingData],
    ) -> None:
        """
        Store document embeddings in Qdrant.
        """

        points = []

        for embedding in embeddings:

            point = PointStruct(
                id=str(uuid4()),

                vector=embedding.embedding,

                payload={
                    "text": embedding.text,
                    "chunk_index": embedding.chunk_index,
                    "page": embedding.page,
                    "source": embedding.source,
                },
            )

            points.append(point)

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=points,
        )