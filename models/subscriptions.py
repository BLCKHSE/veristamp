from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List

from sqlalchemy import TIMESTAMP, Enum as EnumSQL, ForeignKey, Integer, String, ARRAY, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from ..database import db
from ..utils.enums import Currency, ServiceProvider, Status
from ..utils.generators import Generators

@dataclass
class SubscriptionPlan(db.Model):

    __tablename__ = 'subscription_plans'

    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    currency: Mapped[Currency] = mapped_column(EnumSQL(Currency), default=Currency.USD)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    features: Mapped[List[str]] = mapped_column(ARRAY(String))
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    period_in_days: Mapped[int] = mapped_column(Integer())
    plan_url: Mapped[str] = mapped_column(String(180))
    price: Mapped[Decimal] = mapped_column(DECIMAL) 
    provider_plan_id: Mapped[str] = mapped_column(String(45), nullable=False)
    service_provider: Mapped[ServiceProvider] = mapped_column(
        EnumSQL(ServiceProvider, name='service_provider'), default=ServiceProvider.PAYSTACK)
    status: Mapped[Status] = mapped_column(ENUM(Status, create_type=False), default=Status.ACT)
    updated_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    image_url: Mapped[str] = mapped_column(String(200))

    def __repr__(self):
        return f'<SubscriptionPlan (id: {self.id}, name: {self.name}, period_in_days: {self.period_in_days})>'


class SubscriptionOrganisation(db.Model):

    __tablename__ = 'organisation_subscriptions'

    canceled_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    currency: Mapped[Currency] = mapped_column(ENUM(Currency, create_type=False), default=Currency.USD)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    next_billing_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    organisation_id: Mapped[str] = mapped_column(ForeignKey("organisations.id", ondelete='CASCADE'))
    provider_subscription_id: Mapped[str] = mapped_column(String(45), nullable=False, unique=True)
    subscription_customer_id: Mapped[str] = mapped_column(String(45))
    subscription_plan_id: Mapped[str] = mapped_column(ForeignKey("subscription_plans.id"), nullable=True)
    status: Mapped[Status] = mapped_column(ENUM(Status, create_type=False), default=Status.ACT)
    updated_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)

    def __repr__(self):
        return (
            f'<SubscriptionOrganisation (id: {self.id}, '
            + f'organisation: {self.organisation_id}, '
            + f'subscription_plan: {self.subscription_plan_id}, '
            + f'status: {self.status}>'
        )
