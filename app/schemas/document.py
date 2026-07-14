""""
Request Models
Response Models
Internal Data Models"""

from pydantic import BaseModel


class DocumentData(BaseModel):
    """
    Represents the data extracted from a document.
    """

    text: str
    characters: int
    is_empty: bool
    
    pages: int | None = None
    source: str | None = None
