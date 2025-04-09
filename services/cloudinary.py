import cloudinary
import cloudinary.uploader

from ..dtos.cloudinary.file import UploadResponseDTO
from ..settings import CLOUDINARY_API_KEY, CLOUDINARY_CLOUD_NAME, CLOUDINARY_SECRET_KEY


class Cloudinary:

    TEMPLATES_FOLDER = 'vs_templates'

    def __init__(self):
        cloudinary.config(
            cloud_name=CLOUDINARY_CLOUD_NAME,
            api_key=CLOUDINARY_API_KEY,
            api_secret=CLOUDINARY_SECRET_KEY,
            secure=True
        )

    def upload(self, file: str, image_id: str) -> str:
        '''
            Uploads svg to cloudinary as png file

            Parameters:
                - self (StorageCloudinary)
                - file (str): public file url
                - image_id (str)

            Returns:
                - cloudinary image url (str)
        '''
        upload: dict[str, object] = cloudinary.uploader.upload(
            file=file,
            public_id=image_id.removesuffix(".svg"),
            format='png',
            folder=self.TEMPLATES_FOLDER
        )
        upload_response: UploadResponseDTO = UploadResponseDTO(**upload)
        return upload_response.secure_url
