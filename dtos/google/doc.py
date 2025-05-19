from dataclasses import dataclass
from typing import Optional


@dataclass
class Doc:
    '''
    Google docs object
    reference: https://developers.google.com/workspace/add-ons/concepts/event-objects#docs-event-object
    '''

    id: str
    title: str
    url: str
    addon_has_file_scope_permission: Optional[bool] = True
