"""FastAPI dependencies for dependency injection."""
from sqlalchemy.orm import Session
from .database import SessionLocal
from .pdf_service import PDFService
# from .rag_service import RAGService


def get_db():
    """Database session dependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_pdf_service():
    """PDF service dependency."""
    return PDFService()


# def get_rag_service():
#     """RAG service dependency."""
#     return RAGService()
