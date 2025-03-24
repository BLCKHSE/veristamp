from typing import List

from marshmallow import Schema, fields, post_load

from .icon import IconSchema
from ...dtos.google.overflow_menu import OverflowMenu, OverflowMenuItem


class OverflowMenuItemSchema(Schema):
    start_icon: IconSchema = fields.Nested(IconSchema, data_key='startIcon')
    text: str = fields.Str()
    on_click: 'OnClickSchema' = fields.Nested('OnClickSchema') # type: ignore
    disabled: bool = fields.Bool(dump_default=False)

    @post_load
    def make_overflow_menu_item(self, data, **kwargs):
        return OverflowMenuItem(**data)


class OverflowMenuSchema(Schema):
    items: List[OverflowMenuItemSchema] = fields.Nested(OverflowMenuItemSchema, data_key='overflowMenuItem')

    @post_load
    def make_overflow_menu(self, data, **kwargs):
        return OverflowMenu(**data)
