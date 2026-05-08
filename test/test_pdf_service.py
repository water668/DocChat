import sys
import os

from fastapi import UploadFile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.service.pdf_service import PDFService
from src.service.dependencies import get_db
import asyncio

async def upload_dir(dir_name: str):
    db = next(get_db())
    pdf_service = PDFService()
    for file_name in os.listdir(dir_name):
        if not file_name.endswith('.pdf'):
            continue
        _file_name = os.path.join(dir_name, file_name)
        print('Uploading: ', _file_name)
        metadata = await pdf_service.upload_and_process(_file_name, db)


if __name__ == '__main__':
    asyncio.run(upload_dir('data/pdf_repo/'))

