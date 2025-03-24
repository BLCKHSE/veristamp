from typing import List, Literal

from marshmallow import Schema, fields, post_load

from ...dtos.google.column import ColumnItem, Columns
from ...dtos.google.literals import HorizontalAlignment, VerticalAlignment


class ColumnItemSchema(Schema):

    horizontal_alignment: HorizontalAlignment = fields.Str()
    horizontal_size_style: Literal['FILL_AVAILABLE_SPACE', 'FILL_MINIMUM_SPACE'] = fields.Str()
    vertical_alignment: VerticalAlignment = fields.Str()
    widgets: List['WidgetSchema'] = fields.List(fields.Nested('WidgetSchema')) # type: ignore

    @post_load
    def make_column_item(self, data, **kwargs):
        return ColumnItem(**data)


class ColumnsSchema(Schema):

    column_items: List[ColumnItemSchema] = fields.List(fields.Nested(ColumnItemSchema))

    @post_load
    def make_columns(self, data, **kwargs):
        return Columns(**data)
