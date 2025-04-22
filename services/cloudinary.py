from typing import Optional, Union

import cloudinary
import cloudinary.uploader
from werkzeug.datastructures import FileStorage

from ..data.constants import CLOUDINARY_TEMPLATES_FOLDER
from ..dtos.cloudinary.file import UploadResponseDTO
from ..settings import CLOUDINARY_API_KEY, CLOUDINARY_CLOUD_NAME, CLOUDINARY_SECRET_KEY


class Cloudinary:

    def __init__(self):
        cloudinary.config(
            cloud_name=CLOUDINARY_CLOUD_NAME,
            api_key=CLOUDINARY_API_KEY,
            api_secret=CLOUDINARY_SECRET_KEY,
            secure=True
        )

    def upload(
            self, file: Union[str, FileStorage, bytes],
            image_id: str,
            format: Optional[str] = None, 
            folder: str = CLOUDINARY_TEMPLATES_FOLDER) -> str:
        '''
            Uploads svg to cloudinary as png file

            Parameters:
                - self (StorageCloudinary)
                - file (str|FileStorage) : public file url or file object
                - image_id (str)

            Returns:
                - cloudinary image url (str)
        '''
        upload: dict[str, object] = cloudinary.uploader.upload(
            file=file,
            public_id=image_id,
            format=format,
            folder=folder
        )
        upload_response: UploadResponseDTO = UploadResponseDTO(**upload)

        return upload_response.secure_url
