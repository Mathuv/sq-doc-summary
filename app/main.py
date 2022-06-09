import os

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .nlp import summarize_text

N_SUMMARY_SENTENCES = int(os.getenv("N_SUMMARY_SENTENCES", 3))

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/documents/", response_model=schemas.Document)
def create_document(document: schemas.DocumentCreate, db: Session = Depends(get_db)):
    return crud.create_document(db=db, document=document)


@app.get("/documents/", response_model=list[schemas.Document])
def read_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_documents(db=db, skip=skip, limit=limit)


@app.get("/documents/{document_id}", response_model=schemas.Document)
def read_document(document_id: int, db: Session = Depends(get_db)):
    db_document = crud.get_document(db=db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_document


@app.get("/documents/{document_id}/summary/", response_model=schemas.DocumentSummary)
def get_document_summary(document_id: int, db: Session = Depends(get_db)):
    db_document = crud.get_document(db=db, document_id=document_id)
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    summary = summarize_text(text=db_document.text, n_sentences=N_SUMMARY_SENTENCES)
    return schemas.DocumentSummary(
        id=db_document.id, text=db_document.text, summary=summary
    )
