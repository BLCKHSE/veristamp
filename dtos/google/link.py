from dataclasses import dataclass
from typing import Literal


@dataclass
class Link:

    url: str
    title: str

@dataclass
class LinkPreview:

    previewCard: 'Card' # type: ignore
    title: str
    linkPreviewTitle: str


@dataclass
class OpenLink:

    url: str
    open_as: Literal['FULL_SIZE', 'OVERLAY'] = 'OVERLAY'
    on_close: Literal['NOTHING', 'RELOAD'] = 'RELOAD'
