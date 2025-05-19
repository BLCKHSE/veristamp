from typing import Optional

from ..database import db
from ..dtos.google.doc import Doc
from ..models.documents import Document


class DocumentService:

    def create(self, doc: Doc) -> Document:
        document: Document = Document(doc)
        document.save()
        return document

    def get_stamp(self, document_id: str) -> Optional[Document]:
        '''Gets Document entity based on Google Doc Id'''
        return db.session.scalar(db.select(Document).filter_by(provider_document_id=document_id))
