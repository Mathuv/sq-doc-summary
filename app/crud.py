from sqlalchemy.orm import Session

from . import models, schemas


def get_document(db: Session, document_id: int):
    return db.query(models.Document).filter(models.Document.id == document_id).first()


def get_documents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Document).offset(skip).limit(limit).all()


def create_document(db: Session, document: schemas.DocumentCreate):
    db_document = models.Document(text=document.text)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
