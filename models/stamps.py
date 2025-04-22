from datetime import datetime
from typing import Dict, List

from sqlalchemy import JSON, TIMESTAMP, Enum as EnumSQL, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ENUM
from werkzeug.datastructures import ImmutableMultiDict

from ..database import db
from ..dtos.google.literals import InputType
from .user import User
from ..utils.enums import StampEvent, StampItemPosition, StampShape, StampTemplateKey, Status
from ..utils.generators import Generators


class StampTemplateMetadata(db.Model):

    __tablename__ = 'stamp_template_metadata'

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    template_id: Mapped[str] = mapped_column(
        String, 
        ForeignKey("stamp_templates.id", ondelete='CASCADE'),
        nullable=False
    )
    key: Mapped[StampTemplateKey] = mapped_column(
        EnumSQL(StampTemplateKey, name='stamp_template_key'),
        default=StampTemplateKey.MISC,
        nullable=False
    )
    max_size: Mapped[int] = mapped_column(Integer, default=15)
    type: Mapped[InputType] = mapped_column(String, default='TEXT')
    position: Mapped[StampItemPosition] = mapped_column(EnumSQL(StampItemPosition, name='stamp_item_position'), nullable=True)

    def __init__(self, key: StampTemplateKey, max_size: int):
        self.key = key
        self.max_size = max_size

    def __repr__(self) -> str:
        return f'''
            StampTemplateMetadata (id={self.id}, key={self.key}, 
            template={self.template_id}, description={self.description})
            '''
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class StampTemplate(db.Model):

    __tablename__ = 'stamp_templates'

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(60), nullable=False)
    image_url: Mapped[str] = mapped_column(String)
    path_reference: Mapped[str] = mapped_column(String(100), nullable=False)
    shape: Mapped[StampShape] = mapped_column(EnumSQL(StampShape, name='stamp_shape'), default=StampShape.RECTANGLE)
    status: Mapped[Status] = mapped_column(ENUM(Status, create_type=False), default=Status.ACT)
    template_metadata: Mapped[List[StampTemplateMetadata]] = relationship(StampTemplateMetadata, primaryjoin=id==StampTemplateMetadata.template_id)

    def __init__(self, data: ImmutableMultiDict[str, str], image_url: str, dir: str):
        self.name = data.get('name')
        self.description = data.get('description')
        self.shape = data.get('shape')
        self.status = Status.ACT
        self.image_url = image_url
        self.path_reference = dir

    def __repr__(self) -> str:
        return f'StampTemplate (id={self.id}, name={self.name})'
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Stamp(db.Model):

    __tablename__ = 'stamps'

    color_code: Mapped[str] = mapped_column(String(10))
    created_by: Mapped[str] = mapped_column(ForeignKey('users.id'))
    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    creator: Mapped[User] = relationship(User, primaryjoin=created_by==User.id)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[Status] = mapped_column(ENUM(Status, create_type=False), default=Status.ACT)
    template_id: Mapped[str] = mapped_column(ForeignKey("stamp_templates.id"), nullable=False)
    template_content: Mapped[dict] = mapped_column(JSON)
    updated_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    updated_by: Mapped[str] = mapped_column(ForeignKey('users.id'), nullable=True)
    image_url: Mapped[str] = mapped_column(String)

    def __init__(self):
        super().__init__()
        self.status = Status.ACT


class StampApplication(db.Model):
    '''
        Represents stamp usage
    
        Object instance represents each instance a stamp is generated for direct use in a document
    '''

    __tablename__ = 'stamp_applications'

    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    document_id: Mapped[str] = mapped_column(ForeignKey("documents.id"))
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    image_url: Mapped[str] = mapped_column(String)
    stamp_id: Mapped[str] = mapped_column(ForeignKey("stamps.id"), nullable=False)


class StampUser(db.Model):

    __tablename__ = 'stamp_users'

    stamp_id: Mapped[str] = mapped_column(ForeignKey("stamps.id"), primary_key=True, nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), primary_key=True, nullable=False)


class StampAuditLog(db.Model):
    '''Holds logs for stamps + stamp applications'''

    __tablename__ = 'stamp_audit_logs'

    actor_id: Mapped[str] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    document_id: Mapped[str] = mapped_column(ForeignKey("documents.id"))
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    event: Mapped[StampEvent] = mapped_column(EnumSQL(StampEvent, name='stamp_event'), default=StampEvent.GENERAL, nullable=False)
    notes: Mapped[str] = mapped_column(String(150))
    stamp_application_id: Mapped[str] = mapped_column(ForeignKey("stamp_applications.id"), nullable=True)
    stamp_id: Mapped[str] = mapped_column(ForeignKey("stamps.id"), primary_key=True, nullable=True)
