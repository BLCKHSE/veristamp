import enum


class BusinessCategory(enum.Enum):

    RETAIL = 'RETAIL'
    TELECOM = 'TELECOM'
    AGRICULTURE = 'AGRICULTURE'
    REAL_ESTATE = 'REAL ESTATE'
    HOSPITALITY = 'HOSPITALITY'
    TECH = 'TECH'
    BEAUTY= 'BEAUTY'
    HEALTHCARE = 'HEALTHCARE'
    FOOD_AND_BEVERAGE = 'FOOD AND BEVERAGE'
    FASHION = 'FASHION'
    ACCOUNTING_AND_FINANCE = 'ACCOUNTING AND FINANCE'
    LEGAL = 'LEGAL'
    ENTERTAINMENT = 'ENTERTAINMENT'
    GENERAL = 'GENERAL'


class Currency(enum.Enum):

    USD = 'usd'
    EUR = 'eur'
    GBP = 'gbp'
    KES = 'kes'


class PaymentMethod(enum.Enum):

    BANK = 'BANK'
    CARD = 'CARD'
    APPLE_PAY = 'APPLE_PAY'
    GOOGLE_PAY = 'GOOGLE_PAY'
    PAYPAL = 'PAYPAL'
    MOMO = 'MOBILE_MONEY'


class PaystackEvent(enum.Enum):

    INVOICE_CREATE = 'invoice.create'
    INVOICE_PAYMENT_FAIL = 'invoice.payment_failed'
    INVOICE_UPDATE = 'invoice.update'
    SUBSCRIPTION_CREATE = 'subscription.create'
    SUBSCRIPTION_DISABLE = 'subscription.disable'
    SUBSCRIPTION_NOT_RENEW = 'subscription.not_renew'
    SUBSCRIPTION_EXPIRING_CARDS = 'subscription.expiring_cards'
    CHARGE_SUCCESS = 'charge.success'


class ServiceProvider(enum.Enum):

    PAYSTACK = 'paystack'

class Status(enum.Enum):
    '''Represent status enum object data type.'''

    ACT = 'ACTIVE'
    INACT = 'INACTIVE'
    SUSP = 'SUSPENDED'
    ARCH = 'ARCHIVED'
    FLG = 'FLAGGED'


class UserRole(enum.Enum):
    '''Represents user role object datatype'''

    SYS_ADM = 'SYSTEM_ADMIN'
    OWN = 'OWNER'
    ADM = 'ADMIN'
    USR = 'USER'
