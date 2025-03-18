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

class Status(enum.Enum):
    """Represent status enum object data type."""

    ACT = 'ACTIVE'
    INACT = 'INACTIVE'
    SUSP = 'SUSPENDED'
    ARCH = 'ARCHIVED'
    FLG = 'FLAGGED'


class UserRole(enum.Enum):
    """Represents user role object datatype"""

    SYS_ADM = 'SYSTEM_ADMIN'
    OWN = 'OWNER'
    ADM = 'ADMIN'
    USR = 'USER'
