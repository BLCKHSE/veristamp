from dataclasses import dataclass
from typing import Literal, Optional

@dataclass
class UploadResponseDTO:

    api_key: str
    asset_id: str
    bytes: int
    created_at: str
    display_name: str
    etag: str
    format: str
    height: float
    original_filename: str
    placeholder: bool
    public_id: str
    secure_url: str
    signature: str
    tags: list[object]
    type: str
    url: str
    version: int
    version_id: str
    width: float
    asset_folder: Optional[str] = None
    resource_type: Literal['image', 'video'] = 'image'
    original_extension: Optional[str] = None
