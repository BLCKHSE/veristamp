
from marshmallow import Schema, fields


class DocSchema(Schema):
    '''
    Google docs object
    reference: https://developers.google.com/workspace/add-ons/concepts/event-objects#docs-event-object
    '''

    id: str = fields.Str()
    title: str = fields.Str()
    addon_has_file_scope_permission: bool = fields.Bool(data_key='addonHasFileScopePermission')
    url: str = fields.Str()
