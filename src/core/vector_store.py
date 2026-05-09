import logging
from typing import List
from pathlib import Path
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings 
from langchain_chroma import Chroma

logger = logging.getLogger(__name__)

class VectorStore:

    def __init__(self, embedding_model: str='nomic-embed-text', persist_directory: str='data/vectors'):
        self.embeddings = OllamaEmbeddings(model=embedding_model)
        self.persist_directory = persist_directory
        self.vector_db = None
        self.summary_collection_name = '000_-_summary_collection_-_000'
        Path(persist_directory).mkdir(parents=True, exist_ok=True)
        self.summary_db = Chroma(collection_name=self.summary_collection_name, embedding_function=self.embeddings, persist_directory=persist_directory)

    def create_vector_db(self, documents: List, collection_name: str='local-rag') -> Chroma:
        try:
            logger.info(f'Creating vector database with collection: {collection_name}')
            logger.info(f'Persisting to: {self.persist_directory}')
            logger.info(f'Number of documents: {len(documents)}')

            self.vector_db = Chroma.from_documents(
                documents=documents,
                embedding = self.embeddings,
                collection_name = collection_name,
                persist_directory = self.persist_directory
            )
            
            logger.info(f'Vector databse created successfully with {len(documents)} documents')
            return self.vector_db

        except Exception as e:
            logger.error(f'Error creating vector database: {e}')
            raise

    def add_summary(self, summary: str, pdf_collection: str) -> None:
        docs = [Document(page_content=summary, metadata={"pdf_collection": f"{pdf_collection}"})]
        self.summary_db.add_documents(docs)

    def query_summary_collection(self, question: str, top_k: int=3) -> List[Document]:
        print('quesion in query_summary_collection: ', question, top_k)
        try:
            docs_with_scores = self.summary_db.similarity_search_with_score(question, k=top_k)
            return docs_with_scores
        except Exception as e:
            logger.error(f'Error querying summary collection: {e}')
            raise

    def delete_collection(self) -> None:
        if self.vector_db:
            try:
                logger.info('Deleting vector database collection')
                self.vector_db.delete_collection()
                self.vector_db = None
            except Exception as e:
                logger.error(f'Error deleting collection: {e}')
                raise

