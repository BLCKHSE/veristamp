from typing import Optional
from marshmallow import Schema, fields, post_load

from .action import ActionSchema
from .link import OpenLinkSchema
from .overflow_menu import OverflowMenuSchema
from ...dtos.google.on_click import OnClick


class OnClickSchema(Schema):

    action: Optional[ActionSchema] = fields.Nested(ActionSchema)
    open_link: Optional[OpenLinkSchema] = fields.Nested(OpenLinkSchema, data_key='openLink')
    open_dynamic_link_action: Optional[ActionSchema] = fields.Nested(ActionSchema, data_key='openDynamicLinkAction')
    card: Optional['CardSchema'] = fields.Nested('CardSchema') # type: ignore
    overflow_menu: Optional[OverflowMenuSchema] = fields.Nested(OverflowMenuSchema, data_key='overflowMenu')

    @post_load
    def make_on_click(self, data, **kwargs):
        return OnClick(**data)
