

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.core.document import DocumentProcessor, summarize_documents
from langchain_classic.chains.summarize import load_summarize_chain
from src.core.llm import get_llm

if __name__ == '__main__':
    document_processor = DocumentProcessor()
    docs = document_processor.load_pdf('data/vgg.pdf')
    splitted_docs = document_processor.split_documents(docs)
    print('splitted_docs:', len(splitted_docs))
    print('splitted_docs[0]:', splitted_docs[0])
    llm = get_llm('qwen3.5:2b')
    # llm = get_llm('deepseek-chat')
    # summarize_chain = load_summarize_chain(llm, chain_type="stuff", verbose=False)
    # summary = summarize_chain.run(splitted_docs[:4])
    summary = summarize_documents(splitted_docs, llm)
    print('summary:', summary)
