from datetime import datetime
from sqlalchemy import TIMESTAMP, Enum as EnumSQL, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import db
from ..dtos.google.doc import Doc
from ..utils.enums import ServiceProvider
from ..utils.generators import Generators


class Document(db.Model):

    __tablename__ = 'documents'

    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    provider_document_id: Mapped[str] = mapped_column(String(50), nullable=False)
    service_provider: Mapped[ServiceProvider] = mapped_column(
        EnumSQL(ServiceProvider, name='service_provider'), default=ServiceProvider.GOOGLE)
    updated_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    url: Mapped[str] = mapped_column(String(250), nullable=True)

    def __init__(self, doc: Doc):
        super().__init__()
        self.name = doc.title
        self.provider_document_id = doc.id
        self.service_provider = ServiceProvider.GOOGLE
        self.url = doc.url

    def __repr__(self) -> str:
        return f'Document (id={self.id}, name={self.name})'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
