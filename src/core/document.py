"""Document processing functionality."""
import logging
from pathlib import Path
from typing import List
from langchain_community.document_loaders import UnstructuredPDFLoader, PDFMinerLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

class DocumentProcessor:
    """Handles PDF document loading and processing."""
    
    def __init__(self, chunk_size: int = 1500, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    
    def load_pdf(self, file_path: Path) -> List:
        """Load PDF document."""
        try:
            logger.info(f"Loading PDF from {file_path}")
            # loader = UnstructuredPDFLoader(str(file_path))
            loader = PDFMinerLoader(str(file_path))
            return loader.load()
        except Exception as e:
            logger.error(f"Error loading PDF: {e}")
            raise
    
    def split_documents(self, documents: List) -> List:
        """Split documents into chunks."""
        try:
            logger.info("Splitting documents into chunks")
            return self.splitter.split_documents(documents)
        except Exception as e:
            logger.error(f"Error splitting documents: {e}")
            raise

def summarize_documents(documents: List, llm, n_front: int = 4) -> str:
    """Summarize documents using a language model."""
    try:
        logger.info("Summarizing documents")
        from langchain_classic.chains.summarize import load_summarize_chain
        summarize_chain = load_summarize_chain(llm, chain_type="stuff", verbose=False)
        response = summarize_chain.invoke(documents[:n_front])
        return response['output_text']
    except Exception as e:
        logger.error(f"Error summarizing documents: {e}")
        raise