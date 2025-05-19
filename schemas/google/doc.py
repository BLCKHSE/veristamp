
from marshmallow import Schema, fields, post_load

from ...dtos.google.doc import Doc


class DocSchema(Schema):
    '''
    Google docs object
    reference: https://developers.google.com/workspace/add-ons/concepts/event-objects#docs-event-object
    '''

    id: str = fields.Str()
    title: str = fields.Str()
    addon_has_file_scope_permission: bool = fields.Bool(data_key='addonHasFileScopePermission', required=False)
    url: str = fields.Str()

    @post_load
    def make_doc(self, data, **kwargs):
        return Doc(**data)