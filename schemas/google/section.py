from typing import List

from marshmallow import Schema, fields, post_load

from .collapse_control import CollapseControlSchema
from .widget import WidgetSchema
from ...dtos.google.section import Section


class SectionSchema(Schema):

    header: str = fields.Str(required=True)
    collapsible: bool = fields.Bool()
    uncollapsible_widegt_count: int = fields.Int(data_key='uncollapsibleWidgetCount')
    collapse_control: CollapseControlSchema = fields.Nested(CollapseControlSchema, data_key='collapseControl')
    widgets: List[WidgetSchema] = fields.List(fields.Nested(WidgetSchema))

    @post_load
    def make_section(self, data, **kwargs):
        return Section(**data)
