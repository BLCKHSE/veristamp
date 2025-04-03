from datetime import datetime
from sqlalchemy import TIMESTAMP, Enum as EnumSQL, String
from sqlalchemy.orm import Mapped, mapped_column

from ..utils.enums import ServiceProvider
from ..utils.generators import Generators

from ..database import db


class Document(db.Model):

    __tablename__ = 'documents'

    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    provider_document_id: Mapped[str] = mapped_column(String(50), nullable=False)
    service_provider: Mapped[ServiceProvider] = mapped_column(
        EnumSQL(ServiceProvider, name='service_provider'), default=ServiceProvider.GOOGLE)
    updated_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
