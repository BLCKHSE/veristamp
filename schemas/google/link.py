from typing import Literal

from marshmallow import Schema, fields, validate


class LinkSchema(Schema):

    url: str = fields.Str()
    title: str = fields.Str()

class LinkPreviewSchema(Schema):

    preview_card: 'Card'  = fields.Dict(data_key='previewCard') # type: ignore
    title: str = fields.Str() 
    link_preview_title: str = fields.Str(data_key='linkPreviewTitle')


class OpenLinkSchema(Schema):

    url: str = fields.Str()
    open_as: Literal['FULL_SIZE', 'OVERLAY'] = fields.Str(
        validate=[validate.OneOf(choices= ['FULL_SIZE', 'OVERLAY'])])
    on_close: Literal['NOTHING', 'RELOAD'] = fields.Str(
        validate=[validate.OneOf(choices= ['NOTHING', 'RELOAD'])])
