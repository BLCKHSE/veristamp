from typing import Optional
from marshmallow import Schema, fields, post_load, validate

from ...dtos.google.icon import Icon, MaterialIcon
from ...dtos.google.literals import ImageType, KnownIcon


class MaterialIconSchema(Schema):
    name: str = fields.Str()
    weight: int = fields.Int()
    grade: int = fields.Int()
    fill: bool = fields.Bool(dump_default=False)

    @post_load
    def make_material_icon(self, data, **kwargs):
        return MaterialIcon(**data)


class IconSchema(Schema):
    altText: Optional[str] = fields.Str()
    icon_url: Optional[str] = fields.Str(data_key='iconUrl')
    image_type: ImageType =fields.Str(
        data_key='imageType',
        validate=[validate.OneOf(choices= ['CIRCLE', 'SQUARE'])])
    known_icon: Optional[KnownIcon] = fields.Str(data_key='knownIcon')
    material_icon: Optional[MaterialIconSchema] = fields.Nested(MaterialIconSchema, data_key='materialIcon')

    @post_load
    def make_icon(self, data, **kwargs):
        return Icon(**data)
