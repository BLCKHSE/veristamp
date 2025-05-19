from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from .auth import AuthorizationDTO
from .customer import CustomerDTO
from .general import Interval, SubscriptionStatus
from ...utils.enums import PaystackEvent

@dataclass
class SubscriptionEventPlanDTO:

    name: str
    plan_code: str
    description: str
    amount: Decimal
    id: int
    interval: Interval
    send_invoices: bool
    send_sms: bool
    currency: str


@dataclass
class SubscriptionEventDataSourceDTO:

    type: str
    source: str
    entry_point: str
    identifier: Optional[str]


@dataclass
class SubscriptionEventDataDTO:

    authorization: AuthorizationDTO
    customer: CustomerDTO
    domain: str
    id: int
    status: SubscriptionStatus 
    amount: Decimal
    plan: SubscriptionEventPlanDTO
    channel: Optional[str] = None
    created_at: Optional[str] = None
    cron_expression: Optional[str] = None
    currency: Optional[str] = None
    fees: Optional[Decimal] = None
    gateway_response: Optional[str] = None
    ip_address: Optional[str] = None
    most_recent_invoice: Optional[str] = None
    next_payment_date: Optional[str] = None
    open_invoice: Optional[str] = None
    paid_at: Optional[str] = None
    reference: Optional[str] = None
    source: Optional[SubscriptionEventDataSourceDTO] = None
    subscription_code: Optional[str] = None


@dataclass
class SubscriptionEventMetaDTO:

    total: int
    skipped: int
    per_page: int
    page: int
    page_count: int


@dataclass
class SubscriptionEventDTO:

    event: PaystackEvent
    data: SubscriptionEventDataDTO
    meta: Optional[SubscriptionEventMetaDTO] = None
