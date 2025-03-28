from dataclasses import dataclass
from typing import Optional


@dataclass
class CustomerDTO:

    customer_code: str 
    first_name: str
    last_name: str
    email: str
    id: str
    international_format_phone: Optional[str]
    phone: Optional[str]
    metadata: dict[str, object]
    risk_action: str
