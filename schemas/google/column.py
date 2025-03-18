from typing import List, Literal

from marshmallow import Schema, fields

from ...dtos.google.literals import HorizontalAlignment, VerticalAlignment


class ColumnItemSchema(Schema):

    horizontal_alignment: HorizontalAlignment = fields.Str()
    horizontal_size_style: Literal['FILL_AVAILABLE_SPACE', 'FILL_MINIMUM_SPACE'] = fields.Str()
    vertical_alignment: VerticalAlignment = fields.Str()
    widgets: List['Widget'] = fields.Nested('Widget') # type: ignore


class ColumnsSchema:

    column_items: List[ColumnItemSchema] = fields.Nested(ColumnItemSchema)
