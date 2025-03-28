from decimal import Decimal
from typing import Literal, Optional
from marshmallow import EXCLUDE, Schema, fields, post_load

from .auth import AuthorizationSchema
from .customer import CustomerSchema
from ...dtos.paystack.general import SubscriptionStatus
from ...dtos.paystack.subscriptions import (
    SubscriptionEventDTO,
    SubscriptionEventDataDTO,
    SubscriptionEventDataSourceDTO,
    SubscriptionEventPlanDTO
)
from ...utils.enums import PaystackEvent


class SubscriptionEventPlanSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    name: str = fields.String()
    plan_code: str = fields.String()
    description: str = fields.String()
    amount: Decimal = fields.Decimal()
    id: int = fields.Integer()
    interval: Literal['weekly', 'monthly', 'quartely', 'biannually', 'annually'] = fields.String()
    send_invoices: bool = fields.Bool()
    send_sms: bool = fields.Bool()
    currency: str = fields.String()

    @post_load
    def make_subscription_event_plan(self, data, **kwargs):
        return SubscriptionEventPlanDTO(**data)


class SubscriptionEventDataSourceSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    type: str = fields.String()
    source: str = fields.String()
    entry_point: str = fields.String()
    identifier: str = fields.String(allow_none=True)

    @post_load
    def make_subscription_event_data_source(self, data, **kwargs):
        return SubscriptionEventDataSourceDTO(**data)


class SubscriptionEventDataSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    authorization: AuthorizationSchema = fields.Nested(AuthorizationSchema)
    customer: CustomerSchema = fields.Nested(CustomerSchema)
    domain: str = fields.String()
    id: int = fields.Integer()
    status:SubscriptionStatus = fields.String()
    subscription_code: str = fields.String()
    amount: Decimal = fields.Decimal(required=True)
    channel: Optional[str] = fields.String(allow_none=True)
    cron_expression: str= fields.String()
    currency: Optional[str] = fields.String(allow_none=True)
    fees: Optional[Decimal] = fields.Decimal(allow_none=True)
    gateway_response: Optional[str] = fields.String(allow_none=True)
    most_recent_invoice: str = fields.String(allow_none=True)
    ip_address: Optional[str] = fields.String(allow_none=True)
    next_payment_date: str = fields.String()
    open_invoice: str = fields.String(allow_none=True)
    created_at: str = fields.String(data_key='createdAt')
    reference: Optional[str] = fields.String(allow_none=True)
    source: SubscriptionEventDataSourceSchema = fields.Nested(SubscriptionEventDataSourceSchema)
    status: Optional[str] = fields.String(allow_none=True)
    paid_at: str = fields.String(allow_none=True)
    plan: SubscriptionEventPlanSchema = fields.Nested(SubscriptionEventPlanSchema)

    @post_load
    def make_subscription_event_data(self, data, **kwargs):
        return SubscriptionEventDataDTO(**data)
    

class SubscriptionEventMetaSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    total: int = fields.Integer()
    skipped: int = fields.Integer()
    per_page: int = fields.Integer()
    page: int = fields.Integer()
    page_count: int = fields.Integer()


class SubscriptionEventSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    event: PaystackEvent = fields.String()
    data: SubscriptionEventDataSchema = fields.Nested(SubscriptionEventDataSchema)
    meta: SubscriptionEventMetaSchema = fields.Nested(SubscriptionEventMetaSchema)

    @post_load
    def make_subscription_event(self, data, **kwargs):
        return SubscriptionEventDTO(**data)
