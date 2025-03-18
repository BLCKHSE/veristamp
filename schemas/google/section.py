from typing import List

from marshmallow import Schema, fields

from .collapse_control import CollapseControlSchema
from .widget import WidgetSchema



class SectionSchema(Schema):

    header: str = fields.Str(required=True)
    collapsible: bool = fields.Bool()
    uncollapsible_widegt_count: int = fields.Int(data_key='uncollapsibleWidgetCount')
    collapse_control: CollapseControlSchema = fields.Nested(CollapseControlSchema, data_key='collapseControl')
    widgets: List[WidgetSchema] = fields.List(fields.Nested(WidgetSchema))
