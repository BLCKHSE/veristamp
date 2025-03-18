from typing import Literal, Optional
from marshmallow import Schema, fields

from .color import ColorSchema


class BorderStyleSchema(Schema):

    corner_radius: Optional[int] = fields.Int(data_key='cornerRadius')
    stroke_color: Optional[ColorSchema] = fields.Nested(ColorSchema, data_key='strokeColor')
    type: Literal['NO_BORDER', 'STRIKE'] = fields.Str()
