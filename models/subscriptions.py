from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List

from sqlalchemy import TIMESTAMP, Enum as EnumSQL, ForeignKey, Integer, String, ARRAY, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from ..database import db
from ..dtos.paystack.subscriptions import SubscriptionEventDataDTO
from ..utils.enums import Currency, PaymentMethod, PaymentStatus, ServiceProvider, Status
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

    def __init__(
        self, 
        subsciption_data: SubscriptionEventDataDTO, 
        organisation_id: str, 
        subscription_plan_id: str
    ):
        self.created_on = datetime.strptime(subsciption_data.created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.currency = subsciption_data.plan.currency
        self.next_billing_on = datetime.strptime(subsciption_data.next_payment_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.organisation_id = organisation_id
        self.provider_subscription_id = subsciption_data.subscription_code
        self.status = Status.INACT # set to active when 1st payment recieved
        self.subscription_customer_id = subsciption_data.customer.customer_code
        self.subscription_plan_id = subscription_plan_id
        self.updated_on = datetime.now()

    def __repr__(self):
        return f'''
            <SubscriptionOrganisation (id: {self.id},
            organisation: {self.organisation_id},
            subscription_plan: {self.subscription_plan_id},
            +status: {self.status}>
        '''

    def save(self):
        db.session.add(self)
        db.session.commit()



@dataclass
class SubscriptionPayment(db.Model):

    __tablename__ = 'subscription_payments'
    
    amount: Mapped[Decimal] = mapped_column(DECIMAL)
    created_on: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.now)
    currency: Mapped[Currency] = mapped_column(EnumSQL(Currency), default=Currency.USD)
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda:Generators.getAlphaNum(8))
    ip_address: Mapped[str] = mapped_column(String, nullable=True)
    organisation_subscription_id: Mapped[str] = mapped_column(
        ForeignKey("organisation_subscriptions.id", ondelete='CASCADE'))
    payment_method: Mapped[PaymentMethod] = mapped_column(EnumSQL(PaymentMethod), default=PaymentMethod.CARD)
    provider_payment_id: Mapped[str] = mapped_column(String(45), nullable=False, unique=True)
    status: Mapped[PaymentStatus] = mapped_column(EnumSQL(PaymentStatus, name='payment_status'), default=PaymentStatus.COMP)
    status_description: Mapped[str] = mapped_column(String(100))

    def __init__(
        self, 
        subsciption_data: SubscriptionEventDataDTO,
        subscription_id: str
    ):
        self.amount = subsciption_data.amount/100
        self.created_on = datetime.strptime(subsciption_data.paid_at, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.currency = subsciption_data.currency
        self.ip_address = subsciption_data.ip_address
        self.organisation_subscription_id = subscription_id
        self.payment_method = subsciption_data.channel.upper()
        self.provider_payment_id = subsciption_data.reference
        self.status = PaymentStatus.COMP
        self.status_description = subsciption_data.gateway_response

    def save(self):
        db.session.add(self)
        db.session.commit()
