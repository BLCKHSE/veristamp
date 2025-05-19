import enum


class AppsScriptFunction(enum.Enum):

    DASHBOARD = 'onDashboard'
    LANDING = 'onLanding'
    REGISTRATION = 'onRegister'
    REGISTRATION_SUBMIT = 'onRegisterSubmit'
    STAMP_APPLY = 'onStampApply'
    STAMP_APPLY_SUBMIT = 'onStampApplySubmit'
    STAMP_CREATE = 'onStampCreate'
    STAMP_PREVIEW = 'onStampPreview'
    TEMPLATES = 'onTemplates'
    TEMPLATE_SELECT = 'onTemplateSelect'
    USERS = 'onUsers'

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


class MaterialIconName(enum.Enum):

    ADD = 'add_2'
    CORPORATE = 'corporate_fare'
    DOCS_ADD_ON = 'docs_add_on'
    DOWNLOAD = 'download'
    STAMP = 'approval'
    START = 'start'
    PREVIEW = 'preview'


class MenuItem(enum.Enum):

    HOME = 'home'
    DASHBOARD = 'dashboard'
    USERS = 'users'
    SETTINGS = 'settings'
    TEMPLATES = 'templates'


class PaymentMethod(enum.Enum):

    BANK = 'BANK'
    CARD = 'CARD'
    APPLE_PAY = 'APPLE_PAY'
    GOOGLE_PAY = 'GOOGLE_PAY'
    PAYPAL = 'PAYPAL'
    MOMO = 'MOBILE_MONEY'

class PaymentStatus(enum.Enum):

    COMP = 'COMPLETED'
    INIT = 'INITIATED'
    PEND = 'PENDING'
    FAIL = 'FAILED'
    FLG = 'FLAGGED'
    CANC = 'CANCELED'


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
    GOOGLE = 'google'
    MICROSOFT = 'microsoft'


class StampEvent(enum.Enum):

    CREATE = 'CREATE'
    DELETE = 'DELETE'
    EDIT = 'EDIT'
    APPLY = 'APPLY'
    VERIFY = 'VERIFY'
    REPORT = 'REPORT'
    ASSIGN = 'ASSIGN'
    UNASSIGN = 'UNASSIGN'
    GENERAL = 'GENERAL'


class StampItemPosition(enum.Enum):

    TOP = 'top'
    CENTER = 'center'
    BOTTOM = 'bottom'
    LEFT = 'left'
    RIGHT = 'right'


class StampShape(enum.Enum):

    RECTANGLE = 'RECTANGLE'
    SQUARE = 'SQUARE'
    OVAL = 'OVAL'
    CIRCLE = 'CIRCLE'
    HEXAGON = 'HEXAGON'
    TRIANGLE = 'TRIANGLE'
    STAR = 'STAR'


class StampTemplateKey(enum.Enum):

    NAME = 'NAME'
    ADDRESS = 'PHYSICAL ADDRESS'
    POSTAL_ADDRESS = 'POSTAL ADDRESS'
    EMAIL = 'EMAIL'
    PHONE = 'PHONE NUMBER'
    TAGLINE = 'TAGLINE'
    DATE = 'DATE'
    TIMESTAMP = 'TIMESTAMP'
    ID = 'ID NUMBER'
    MISC = 'MISCALLANEOUS'
    ROLE = 'ROLE'


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
