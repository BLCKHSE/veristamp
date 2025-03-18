from typing import List

from marshmallow import Schema, fields

from .icon import IconSchema


class OverflowMenuItemSchema(Schema):
    start_icon: IconSchema = fields.Nested(IconSchema, data_key='startIcon')
    text: str = fields.Str()
    on_click: 'OnClick' = fields.Dict() # type: ignore
    disabled: bool = fields.Bool(dump_default=False)


class OverflowMenuSchema(Schema):
    items: List[OverflowMenuItemSchema] = fields.Nested(OverflowMenuItemSchema)
