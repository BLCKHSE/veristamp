from typing import Optional
from marshmallow import EXCLUDE, Schema, fields, post_load

from ...dtos.paystack.customer import CustomerDTO


class CustomerSchema(Schema):

    class Meta:
        unknown = EXCLUDE

    first_name: str = fields.String()
    last_name: str = fields.String()
    email: str = fields.Email()
    customer_code: str  = fields.String()
    id: int = fields.Integer()
    international_format_phone: Optional[str] = fields.String(allow_none=True)
    phone: str = fields.String()
    metadata: dict[str, object] = fields.Dict(required=False, allow_none=True)
    risk_action: str = fields.String()

    @post_load
    def make_customer(self, data, **kwargs):
        return CustomerDTO(**data)
