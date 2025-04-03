from datetime import datetime
from typing import List

from sqlalchemy import JSON, TIMESTAMP, Enum as EnumSQL, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ENUM

from ..database import db
from ..utils.enums import StampEvent, StampShape, StampTemplateKey, Status
from ..utils.generators import Generators


class StampTemplate(db.Model):

    __tablename__ = 'stamp_templates'

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(60), nullable=False)
    shape: Mapped[StampShape] = mapped_column(EnumSQL(StampShape, name='stamp_shape'), default=StampShape.RECTANGLE)
    template_metadata: Mapped[List['StampTemplateMetadata']] = relationship()
    path_reference: Mapped[str] = mapped_column(String(100), nullable=False)


class StampTemplateMetadata(db.Model):

    __tablename__ = 'stamp_template_metadata'

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    template_id: Mapped[str] = mapped_column(ForeignKey("stamp_templates.id"), nullable=False)
    key: Mapped[StampTemplateKey] = mapped_column(EnumSQL(StampTemplateKey, name='stamp_template_key'), default=StampTemplateKey.MISC, nullable=False)
    max_size: Mapped[int] = mapped_column(Integer, default=15) 


class Stamp(db.Model):

    __tablename__ = 'stamps'

    color_code: Mapped[str] = mapped_column(String(10))
    created_by: Mapped[str] = mapped_column(ForeignKey('users.id'))
    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[Status] = mapped_column(ENUM(Status, create_type=False), default=Status.ACT)
    template_id: Mapped[str] = mapped_column(ForeignKey("stamp_templates.id"), nullable=False)
    template_content: Mapped[dict] = mapped_column(JSON)
    updated_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    updated_by: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=True)


class StampUser(db.Model):

    __tablename__ = 'stamp_users'

    stamp_id: Mapped[str] = mapped_column(ForeignKey("stamps.id"), primary_key=True, nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), primary_key=True, nullable=False)


class StampAuditLog(db.Model):

    __tablename__ = 'stamp_audit_logs'

    actor_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    document_id: Mapped[str] = mapped_column(ForeignKey("documents.id"))
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    event: Mapped[StampEvent] = mapped_column(EnumSQL(StampEvent, name='stamp_event'), default=StampEvent.GENERAL, nullable=False)
    notes: Mapped[str] = mapped_column(String(150))
    stamp_id: Mapped[str] = mapped_column(ForeignKey("stamps.id"), nullable=False)
