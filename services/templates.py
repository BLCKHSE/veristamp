from datetime import datetime
import json
from os import mkdir, path
from typing import Dict, List, Tuple

from werkzeug.datastructures import ImmutableMultiDict, FileStorage

from ..database import db
from ..dtos.google.card import Card
from ..dtos.google.chips import ChipList
from ..dtos.google.grid import Grid
from ..dtos.google.header import Header
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget
from ..models.stamps import StampTemplate, StampTemplateMetadata
from ..services.navigation import NavigationService
from ..settings import BASE_URL
from ..utils.enums import MenuItem, Status
from .cloudinary import Cloudinary


class TemplateService:

    CARD_ID_TEMPLATES = 'templates.main'
    TEMPLATES_DIR = './static/templates'

    def __init__(self):
        self._navigation_service = NavigationService()
        self._cloudinary_service = Cloudinary()

    def _get_templates_grid(self, templates: List[StampTemplate]) -> Grid:
        pass

    def _save_template_file(self, file: FileStorage) -> str:
        '''Saves template svg file'''

        filename: str = f'{file.filename.removesuffix(".svg")}_{int(datetime.now().timestamp())}.svg'
        file_path = path.join(self.TEMPLATES_DIR, filename)
        if not path.isdir(self.TEMPLATES_DIR):
            mkdir(self.TEMPLATES_DIR)
        file.save(file_path)
        file.close()

        return filename

    def create(self, data: ImmutableMultiDict[str, str], template_file: FileStorage) -> Tuple[StampTemplate, Dict[str, str]]:
        '''Creates a template record and the corresponding metadata records

            Parameters:
                - self (TemplateService)
                - data (ImmutableMultiDict[str, str]): Template form data
                - template_file (FileStorage)
            
            Returns:
                template, errors (Tuple[StampTemplate, Dict[str, str]])
        '''
        errors: dict[str, object] = {}
        template: StampTemplate  = None
        try:
            filename: str = self._save_template_file(template_file)
            template_image_url: str = self._cloudinary_service.upload(
                file=path.join(f'{BASE_URL}{self.TEMPLATES_DIR.replace(".", "")}', filename), 
                image_id=filename
            )
            # template_image_url: str = 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744191455/vs_templates/rect_1744191453.png'

            template = StampTemplate(
                data=data,
                image_url=template_image_url,
                dir=path.join(f'{self.TEMPLATES_DIR.replace(".", "")}', filename)
            )
            metadata: list[dict[str, object]] = json.loads(data.get('metadata'))
            template_metadata: list[StampTemplateMetadata] = [StampTemplateMetadata(entry.get('key'), entry.get('maxSize')) for entry in metadata]
            template.template_metadata.extend(template_metadata)
            db.session.add(template)
            db.session.add_all(template_metadata)
            db.session.commit()
        except Exception as err:
            errors = err

        return template, errors

    def get_templates(self) -> List[StampTemplate]:
        return db.session.scalars(db.select(StampTemplate).filter_by(status=Status.ACT)).all()

    def get_tamplates_card(self) -> Card:
        menu: ChipList = self._navigation_service.get_menu(active_page=MenuItem.TEMPLATES)
        menu_section: Section = Section(header=None, widgets=[Widget(chip_list=menu)])
        templates: List[StampTemplate] = self.get_templates()
        # create templates card
        card: Card = Card(
            name=self.CARD_ID_TEMPLATES,
            header=Header(self.CARD_SUBTITLE_TEMPLATES),
            sections=[menu_section]
        )
        return card
