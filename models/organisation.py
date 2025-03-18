from typing import List, Optional

from sqlalchemy import Enum as EnumSQL, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import db
from ..utils.enums import BusinessCategory
from ..utils.generators import Generators


class Organisation(db.Model):

    __tablename__ = 'organisations'

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    category: Mapped[BusinessCategory] = mapped_column(EnumSQL(BusinessCategory), default=BusinessCategory.GENERAL)
    name: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    google_organisation_id: Mapped[str] = mapped_column(String(30), unique=True, nullable=True)
    users: Mapped[List['User']] = relationship() # type: ignore
    website_url: Mapped[str] = mapped_column(String(200), nullable=True)

    def __init__(self, name: str, category: BusinessCategory, website: Optional[str]):
        self.category = category
        self.name = name
        self.website_url = website

    def __repr__(self) -> str:
        return f'Organisation (id={self.id}, name={self.name})'
    
    def save(self):
        db.session.add(self)
        db.session.commit()
