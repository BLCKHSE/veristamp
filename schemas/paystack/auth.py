from typing import Optional
from marshmallow import Schema, fields, post_load

from ...dtos.paystack.auth import AuthorizationDTO


class AuthorizationSchema(Schema):

    account_name: str = fields.String(required=False, allow_none=True)
    authorization_code: str = fields.String()
    bin: str = fields.String()
    last4: str = fields.String()
    expiry_month: str = fields.String(data_key='exp_month') 
    expiry_year: str = fields.String(data_key='exp_year') 
    card_type: str = fields.String()
    bank: str = fields.String()
    country_code: str = fields.String()
    brand: str = fields.String()
    channel: str = fields.String()
    receiver_bank_account_number: Optional[str] = fields.String(allow_none=True)
    receiver_bank: Optional[str] = fields.String(allow_none=True)
    reusable: bool = fields.Boolean()
    signature: str = fields.String()

    @post_load
    def make_auth(self, data, **kwargs):
        return AuthorizationDTO(**data)
