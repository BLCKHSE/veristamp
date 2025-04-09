from flask import jsonify, request
from flask.views import MethodView
from marshmallow import ValidationError
from werkzeug.datastructures import ImmutableMultiDict, FileStorage

from ..dtos.google.action_render import ActionRender, Navigation
from ..dtos.google.card import Card
from ..services.templates import TemplateService
from ..schemas.google.action_render_schema import ActionRenderSchema
from ..schemas.templates.template import TemplateFileSchema, TemplateSchema
from ..utils.decorators import authenticate


class TemplateAddonAPI(MethodView):

    init_every_request = False
    
    def __init__(self):
        super().__init__()
        self.response_schema = ActionRenderSchema()
        self._templates_service = TemplateService()

    @authenticate
    def post(self, **kwargs):
        templates_card: Card = self._templates_service.get_tamplates_card()

        render_action: ActionRender = ActionRender(Navigation(push_card=templates_card))
        return jsonify(self.response_schema.dump(render_action)), 200
    

class TemplateApi(MethodView):

    init_every_request = False
    
    def __init__(self):
        super().__init__()
        self._file_schema = TemplateFileSchema()
        self._template_schema = TemplateSchema()
        self._template_service = TemplateService()

    def post(self, **kwargs):
        try:
            data: ImmutableMultiDict[str, str] = self._template_schema.load(request.form)
            files: ImmutableMultiDict[str, FileStorage] = self._file_schema.load(request.files)
            template_file: FileStorage = files.get('file')
            template, errors = self._template_service.create(data, template_file)
            if len(errors):
                raise ValidationError(errors)
            return jsonify(self._template_schema.dump(template)), 200
        except ValidationError as e:
            return jsonify(e.messages), 400
        except Exception as e:
            print(e)
            return jsonify({'error': 'Something went wrong. Check request details again and try again.'}), 500
