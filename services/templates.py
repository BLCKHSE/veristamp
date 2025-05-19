import json
from datetime import datetime
from os import mkdir, path
from typing import Dict, List, Optional, Tuple

from werkzeug.datastructures import ImmutableMultiDict, FileStorage

from .cloudinary import Cloudinary
from ..database import db
from ..data.constants import ADD_STAMP_URI, CARD_ID_TEMPLATES, SUBTITLE_CARD_TEMPLATES, TEMPLATES_DIR
from ..dtos.google.action import Action
from ..dtos.google.border import BorderStyle
from ..dtos.google.card import Card
from ..dtos.google.chips import ChipList
from ..dtos.google.grid import Grid, GridItem
from ..dtos.google.header import Header
from ..dtos.google.image import ImageComponent
from ..dtos.google.literals import GoogleSource
from ..dtos.google.on_click import OnClick
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget
from ..models.stamps import StampTemplate, StampTemplateMetadata
from ..services.navigation import NavigationService
from ..settings import BASE_URL
from ..utils.enums import AppsScriptFunction, MenuItem, Status


class TemplateService:

    def __init__(self):
        self._navigation_service = NavigationService()
        self._cloudinary_service = Cloudinary()

    def _get_templates_grid(self, templates: List[StampTemplate], source: GoogleSource = 'ADDON') -> Grid:
        items: List[GridItem] = []
        for template in templates:
            image_component: ImageComponent = ImageComponent(
                image_uri=template.image_url, alt_text=template.description, border_style=None)
            item: GridItem = GridItem(
                id=template.id, title=template.name, image=image_component, text_alignment='END')
            items.append(item)

        item_onclick: OnClick = OnClick(action=Action(
            function=(
                f'{BASE_URL}{ADD_STAMP_URI}') if source =='ADDON' else AppsScriptFunction.TEMPLATE_SELECT.value
            )
        )
        grid_border_style: BorderStyle = BorderStyle(corner_radius=5, type='STROKE')
        templates_grid: Grid = Grid(
            column_count=2,
            items=items,
            on_click=item_onclick,
            border_style=grid_border_style
        )

        return templates_grid

    def _save_template_file(self, file: FileStorage) -> str:
        '''Saves template svg file'''

        filename: str = f'{file.filename.removesuffix(".svg")}_{int(datetime.now().timestamp())}.svg'
        file_path = path.join(TEMPLATES_DIR, filename)
        if not path.isdir(TEMPLATES_DIR):
            mkdir(TEMPLATES_DIR)
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
                file=path.join(f'{BASE_URL}{TEMPLATES_DIR.replace(".", "")}', filename), 
                image_id=filename.removesuffix(".svg"),
                format='png'
            )
            # template_image_url: str = 'https://res.cloudinary.com/dr5li7c0i/image/upload/v1744191455/vs_templates/rect_1744191453.png'

            template = StampTemplate(
                data=data,
                image_url=template_image_url,
                dir=path.join(f'{TEMPLATES_DIR.replace(".", "")}', filename)
            )
            metadata: list[dict[str, object]] = json.loads(data.get('metadata'))
            template_metadata: list[StampTemplateMetadata] = [
                StampTemplateMetadata(entry.get('key'), entry.get('maxSize')) for entry in metadata
            ]
            template.template_metadata.extend(template_metadata)
            db.session.add(template)
            db.session.add_all(template_metadata)
            db.session.commit()
        except Exception as err:
            errors = err

        return template, errors

    def get_template(self, template_id: str) -> Optional[StampTemplate]:
        return db.session.scalar(db.select(StampTemplate).filter_by(id=template_id))

    def get_templates(self) -> List[StampTemplate]:
        return db.session.scalars(db.select(StampTemplate).filter_by(status=Status.ACT)).all()

    def get_tamplates_card(self, source: GoogleSource = 'ADDON') -> Card:
        menu: ChipList = self._navigation_service.get_menu(active_page=MenuItem.TEMPLATES, source=source)
        menu_section: Section = Section(header=None, widgets=[Widget(chip_list=menu)])
        templates: List[StampTemplate] = self.get_templates()

        templates_section: Section = Section(
            header='Select Template',
            widgets=[Widget(grid=self._get_templates_grid(templates, source))]
        )
        card: Card = Card(
            name=CARD_ID_TEMPLATES,
            header=Header(SUBTITLE_CARD_TEMPLATES),
            sections=[menu_section, templates_section]
        )
        return card
