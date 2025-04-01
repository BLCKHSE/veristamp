from dataclasses import dataclass
from typing import List, Literal, Optional

from marshmallow import Schema, fields, post_load

from .icon import IconSchema
from .on_click import OnClickSchema
from ...dtos.google.chips import Chip, ChipList


class ChipSchema(Schema):

    on_click: OnClickSchema = fields.Nested(OnClickSchema, data_key='onClick')
    icon: Optional[IconSchema] = fields.Nested(IconSchema)
    alt_text: Optional[str] = fields.Str(data_key='altText')
    disabled: bool = fields.Boolean()
    label: Optional[str] = fields.Str()

    @post_load
    def make_chip(self, data, **kwargs):
        return Chip(**data)


class ChipListSchema(Schema):

    chips: List[ChipSchema] = fields.List(fields.Nested(ChipSchema))
    layout: Literal['WRAPPED', 'HORIZONTAL_SCROLLABLE'] = fields.Str()

    @post_load
    def make_chip_list(self, data, **kwargs):
        return ChipList(**data)
