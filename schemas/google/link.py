from typing import Literal

from marshmallow import Schema, fields, post_load, validate

from ...dtos.google.link import Link, LinkPreview, OpenLink


class LinkSchema(Schema):

    url: str = fields.Str()
    title: str = fields.Str()

    @post_load
    def make_link(self, data, **kwargs):
        return Link(**data)

class LinkPreviewSchema(Schema):

    preview_card: 'Card'  = fields.Dict(data_key='previewCard') # type: ignore
    title: str = fields.Str() 
    link_preview_title: str = fields.Str(data_key='linkPreviewTitle')

    @post_load
    def make_link_preview(self, data, **kwargs):
        return LinkPreview(**data)


class OpenLinkSchema(Schema):

    url: str = fields.Str()
    open_as: Literal['FULL_SIZE', 'OVERLAY'] = fields.Str(
        data_key='openAs',
        validate=[validate.OneOf(choices= ['FULL_SIZE', 'OVERLAY'])])
    on_close: Literal['NOTHING', 'RELOAD'] = fields.Str(
        data_key='onClose',
        validate=[validate.OneOf(choices= ['NOTHING', 'RELOAD'])])

    @post_load
    def make_open_link(self, data, **kwargs):
        return OpenLink(**data)
