from dataclasses import dataclass


@dataclass
class Doc:
    '''
    Google docs object
    reference: https://developers.google.com/workspace/add-ons/concepts/event-objects#docs-event-object
    '''

    id: str
    title: str
    addon_has_file_scope_permission: bool
    url: str
