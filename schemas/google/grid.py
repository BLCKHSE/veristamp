from typing import List, Literal, Optional
from marshmallow import Schema, fields, post_load

from .border import BorderStyleSchema
from .image import ImageComponentSchema
from .on_click import OnClickSchema
from ...dtos.google.grid import Grid, GridItem


class GridItemSchema(Schema):
    id: str = fields.Str()
    image: ImageComponentSchema = fields.Nested(ImageComponentSchema)
    layout: Literal['TEXT_BELOW', 'TEXT_ABOVE'] = fields.Str()
    title: str = fields.Str()
    subtitle: Optional[str] = fields.Str()

    @post_load
    def make_grid_item(self, data, **kwargs):
        return GridItem(**data)


class GridSchema(Schema):

    column_count: int = fields.Int(data_key='columnCount')
    border_style: BorderStyleSchema = fields.Nested( BorderStyleSchema, data_key='borderStyle')
    title: str = fields.Str()
    items: List[GridItemSchema] = fields.List(fields.Nested(GridItemSchema))
    on_click: OnClickSchema = fields.Nested(OnClickSchema, data_key='onClick')

    @post_load
    def make_grid(self, data, **kwargs):
        return Grid(**data)
