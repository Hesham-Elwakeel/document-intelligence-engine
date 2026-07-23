from pydantic import BaseModel

from app.schemas.document import DocumentData


class PipelineResult(BaseModel):
    """
    Represents the final output of the document processing pipeline.
    """

    pipeline: str
    decision: str
    document: DocumentData