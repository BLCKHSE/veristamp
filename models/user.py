from datetime import datetime

from sqlalchemy import TIMESTAMP, Enum as EnumSQL, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from ..database import db
from ..utils.enums import Status, UserRole
from ..utils.generators import Generators

class User(db.Model):

    __tablename__ = 'users'

    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    country_code: Mapped[str] = mapped_column(String(2), nullable=True)
    email: Mapped[str] = mapped_column(String(45), unique=True, nullable=False)
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, nullable=True)
    first_name: Mapped[str] = mapped_column(String(15))
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    last_name: Mapped[str] = mapped_column(String(15))
    organisation_id: Mapped[str] = mapped_column(ForeignKey("organisations.id", ondelete='CASCADE'))
    role: Mapped[UserRole] = mapped_column(EnumSQL(UserRole), default=UserRole.USR)
    status: Mapped[Status] = mapped_column(EnumSQL(Status), default=Status.ACT)
    timezone: Mapped[str] = mapped_column(String)
    updated_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)

    def __init__(self, data: dict[str, object]):
        self.created_on = datetime.now()
        self.email = data.get('email')
        self.first_name = data.get('first_name')
        self.last_name = data.get('last_name')
        self.status = Status.ACT
        self.timezone = data.get('time_zone')

    def __repr__(self) -> str:
        return f'User (id={self.id}, email={self.email})'
    
    @property
    def full_name(self) -> str:
        name: str = ''
        name +=  self.first_name if self.first_name != None and len(self.first_name) > 0 else ''
        name +=  (' ' + self.last_name) if self.last_name != None and  len(self.last_name) > 0 else ''
        return name.upper
    
    def save(self):
        db.session.add(self)
        db.session.commit()
