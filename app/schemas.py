from pydantic import BaseModel


class DocumentBase(BaseModel):
    text: str


class DocumentCreate(DocumentBase):
    pass


class DocumentCreateResponse:
    """Response schema for the API to create new document"""
    id: int

    class Config:
        orm_mode = True


class Document(DocumentBase):
    """Response schema for the get document(s)"""

    id: int

    class Config:
        orm_mode = True

class DocumentSummary(BaseModel):
    """Response schema for the get the document summary"""
    id: int
    text: str
    summary: str

    class Config:
        orm_mode = True
