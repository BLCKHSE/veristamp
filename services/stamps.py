from datetime import datetime
from typing import Optional, Tuple

from ..data.constants import (
    CARD_ID_CREATE_STAMP,
    CLOUDINARY_STAMPS_FOLDER, 
    COLOR_CODES, 
    STAMPS_PREVIEW_URI,
    STAMPS_URI, 
    SUBTITLE_CARD_CREATE_STAMP,
)
from ..database import db
from ..dtos.google.action import Action, ActionParameter
from ..dtos.google.button import Button
from ..dtos.google.card import Card
from ..dtos.google.chips import ChipList
from ..dtos.google.decorated_text import DecoratedText
from ..dtos.google.footer import Footer
from ..dtos.google.general import FormInput
from ..dtos.google.icon import Icon, MaterialIcon
from ..dtos.google.image import Image
from ..dtos.google.input import SelectionInput, SelectionItem, TextInput, Validation
from ..dtos.google.header import Header
from ..dtos.google.on_click import OnClick
from ..dtos.google.section import Section
from ..dtos.google.widget import Widget
from ..models.stamps import Stamp, StampTemplate, StampTemplateMetadata
from ..models.user import User
from ..services.cloudinary import Cloudinary
from ..services.templates import TemplateService
from ..services.user import UserService
from ..services.navigation import NavigationService
from ..settings import BASE_URL, THEME_PRIMARY_COLOUR
from ..utils.enums import MaterialIconName, MenuItem


class StampService:

    _GENERAL_INPUTS = ['STAMP_NAME', 'COLOUR']

    def __init__(self):
        self._cloudinary_service = Cloudinary()
        self._navigation_service = NavigationService()
        self._required_create_stamp_inputs = ['stamp_name']
        self._template_service = TemplateService()
        self._user_service = UserService()

    def _get_create_stamp_form(self, template: StampTemplate) -> Section:
        '''Generates stamp form based on provided stamp template
        
            Returns:
                inputs (Section)
        '''
        form_input_widgets: list[Widget] = []
        template_metadata: list[StampTemplateMetadata] = template.template_metadata
        for metadata in template_metadata:
            text_validation: Validation = Validation(
                character_limit=metadata.max_size, 
                input_type=metadata.type if metadata.type != None else 'TEXT'
            )
            input_name: str = metadata.key.name
            input_change_action: Action = Action(function='onChangeTextInput', required_widgets=[input_name])
            text_input: TextInput = TextInput(
                label=metadata.key.value,
                hint_text=f'As displayed on the {metadata.position.value.upper() + " of the" if metadata.position != None else "" } stamp ',
                name=input_name,
                validation=text_validation,
                on_change_action=input_change_action,
            )
            self._required_create_stamp_inputs.append(input_name)
            form_input_widgets.append(Widget(text_input=text_input))

        form_section: Section = Section(header='Enter Stamp Template Details', widgets=form_input_widgets)
        return form_section
    
    def _get_create_stamp_general_inputs(self) -> Section:
        '''Gets a list of the general stamp inputs, eg. colour code, internal name
        
            Returns:
                inputs (list[Widget])
        '''
        input_widgets: list[Widget] = []
        name_input: TextInput = TextInput(
            label='STAMP NAME',
            name='STAMP_NAME',
            hint_text='Stamp reference, for internal use only',
            validation=Validation(30,'TEXT'),
            on_change_action=Action(function='onChangeTextInput', required_widgets=['stamp_name']),
        )
        input_widgets.append(Widget(text_input=name_input))
        color_input: SelectionInput = SelectionInput(
            label='COLOR CODE',
            name='COLOUR',
            type='MULTI_SELECT',
            on_change_action=Action(function='onChangeTextInput', required_widgets=['colour_code']),
            multi_select_max_selected_items=1,
            multi_select_min_query_length=1,
            items=[SelectionItem(
                text=color.get('code'), 
                value=color.get('code'), 
                start_icon_uri=color.get('icon_url'),
                selected=color.get('code')==THEME_PRIMARY_COLOUR
            ) for color in COLOR_CODES],
        )
        input_widgets.append(Widget(selection_input=color_input))

        return Section(header='Addtional Stamp Details', widgets=input_widgets)

    def _get_create_stamp_template_view(self, template: StampTemplate) -> Section:
        '''Generates stamp template display section. Includes template image, name & description

            Parameters:
                - self (StampService)
                - tamplate (StampTemplate)

            Returns:
                template_display (Section)
        '''
        template_image_widget: Image = Image(alt_text=f'{template.name} Image', image_url=template.image_url)
        about_template_widget: DecoratedText = DecoratedText(
            text=template.name,
            wrap_text=True,
            top_label=template.description,
            start_icon=Icon(alt_text='Stamp Template Icon', material_icon=MaterialIcon(MaterialIconName.STAMP.value))
        )

        template_view_section: Section =  Section(
            header='Selected Template',
            widgets=[Widget(image=template_image_widget), Widget(decorated_text=about_template_widget)]
        )
        return template_view_section
    
    def _get_stamp_form_submit_footer(self, template_id: str) -> Footer:
        '''Gets fixed card footer with "PREVIEW" & "SUBMIT" form buttons
        
            Returns:
                inputs (Footer)
        '''
        submit_btn: Button = Button(
            alt_text='Submit Create Stamp Form',
            text='SUBMIT',
            on_click=OnClick(action=Action(
                function=f'{BASE_URL}/{STAMPS_URI}?t_id={template_id}',
                required_widgets=self._required_create_stamp_inputs
            ))
        )
        preview_btn: Button = Button(
            alt_text='Preview Stamp in web Before Creation',
            color=None,
            text='PREVIEW',
            icon=Icon(material_icon=MaterialIcon(name=MaterialIconName.PREVIEW.value)),
            type='OUTLINED',
            on_click=OnClick(
                open_dynamic_link_action=Action(
                    function=f'{BASE_URL}/{STAMPS_PREVIEW_URI}', 
                    parameters=[ActionParameter(template_id, template_id)]
                )
            )
        )
        form_footer: Footer = Footer(
            primary_button=submit_btn,
            secondary_button=preview_btn
        )
        return form_footer

    def _get_variable_filled_stamp(
        self, 
        template: StampTemplate,
        form_inputs: dict[str, FormInput],
        timezone: Optional[str] = None
    ) -> str:
        '''Interpolates template variables into stamp
                    
            Parameters:
                - self (StampService)
                - tamplate (StampTemplate)
                - form_inputs (dict[str, FormInput])

            Returns:
                updated_template (str)
        '''

        template_file = open('.' + template.path_reference)
        date_format: str = '%m-%d-%Y' if timezone != None and timezone.startswith('US/') else '%d-%m-%Y'
        template_metadata: dict[str, str] = {'DATE': datetime.now().strftime(date_format)}
        for metadata in template.template_metadata:
            template_metadata[metadata.key.name] = form_inputs[metadata.key.name].stringInputs.value[0]
        updated_template: str = template_file.read().format(**template_metadata)

        return updated_template

    def create(self, template_id: str, form_inputs: dict[str, FormInput], creator_email: Optional[str]) -> Tuple[Stamp, Optional[dict[str, str]]]:
        '''Creates a client specific stamp record to be used when applying stamps to documents
        '''
        template: Optional[StampTemplate] = self._template_service.get_template(template_id)
        if template == None:
            return None, {'template', "Template not found"}
        user: Optional[User] = self._user_service.get_user(creator_email)
        errors: dict[str, object] = {}
        stamp: Stamp = None 
        try: 
            stamp_url: str = self._cloudinary_service.upload(
                file=self._get_variable_filled_stamp(template=template, form_inputs=form_inputs).encode(), 
                image_id=f'{template.id}_{user.id}_{int(datetime.now().timestamp())}',
                folder=f'{CLOUDINARY_STAMPS_FOLDER}/{user.organisation_id}'
            )

            stamp = Stamp()
            stamp.color_code = form_inputs.get('COLOUR').stringInputs.value[0]
            stamp.created_by = user.id
            stamp.image_url = stamp_url
            stamp.name = form_inputs.get('STAMP_NAME').stringInputs.value[0]
            stamp.template_id = template_id
            stamp.template_content = {
                key: val.stringInputs.value[0] for key, val in form_inputs.items() if key not in self._GENERAL_INPUTS
            }
            stamp.updated_by = user.id
            db.session.add(stamp)
            db.session.commit()
        except Exception as err:
            errors = err

        return stamp, errors
    
    def get_create_stamp_card(self, template: StampTemplate) -> Card:
        menu: ChipList = self._navigation_service.get_menu(active_page=MenuItem.TEMPLATES)
        menu_section: Section = Section(header=None, widgets=[Widget(chip_list=menu)])
        template_view_section: Section = self._get_create_stamp_template_view(template=template)
        form_section: Section = self._get_create_stamp_form(template)
        secondary_form_section: Section = self._get_create_stamp_general_inputs()
        
        card: Card = Card(
            name=CARD_ID_CREATE_STAMP,
            header=Header(SUBTITLE_CARD_CREATE_STAMP),
            sections=[menu_section, template_view_section, form_section, secondary_form_section],
            fixed_footer=self._get_stamp_form_submit_footer(template.id)
        )
        return card
