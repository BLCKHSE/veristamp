from typing import Optional
from marshmallow import Schema, fields

from .action import ActionSchema
from .link import OpenLinkSchema
from .overflow_menu import OverflowMenuSchema


class OnClickSchema(Schema):

    action: Optional[ActionSchema] = fields.Nested(ActionSchema)
    open_link: Optional[OpenLinkSchema] = fields.Nested(OpenLinkSchema)
    open_dynamic_link_action: Optional[ActionSchema] = fields.Nested(ActionSchema)
    card: Optional['Card'] = fields.Dict() # type: ignore
    overflow_menu: Optional[OverflowMenuSchema]
