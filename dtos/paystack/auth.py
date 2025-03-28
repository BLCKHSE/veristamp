from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthorizationDTO:

    account_name: str
    authorization_code: str
    bin: str
    last4: str
    expiry_month: str
    expiry_year: str
    card_type: str
    bank: str
    country_code: str
    brand: str
    channel: str
    reusable: bool
    signature: str
    receiver_bank_account_number: Optional[str] = None
    receiver_bank: Optional[str] = None
