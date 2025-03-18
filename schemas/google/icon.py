from typing import Optional
from marshmallow import Schema, fields, validate

from ...dtos.google.literals import ImageType, KnownIcon


class MaterialIconSchema(Schema):
    name: str = fields.Str()
    weight: int = fields.Int()
    grade: int = fields.Int()
    fill: bool = fields.Bool(dump_default=False)


class IconSchema(Schema):
    altText: Optional[str] = fields.Str()
    icon_url: Optional[str] = fields.Str()
    image_type: ImageType =fields.Str(
        validate=[validate.OneOf(choices= ['CIRCLE', 'SQUARE'])])
    known_icon: Optional[KnownIcon] = fields.Str()
    material_icon: Optional[MaterialIconSchema] = fields.Nested(MaterialIconSchema)
