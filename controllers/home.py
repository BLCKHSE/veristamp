from flask import jsonify, request
from flask.views import MethodView

from ..services.home import HomeService
from ..utils.decorators import authenticate


class HomeAPI(MethodView):

    init_every_request = False

    @authenticate
    def post(self, **kwargs):
        # TODO: Check if user already exists, if no "redirect" to main page
        card = HomeService().get_welcome_screen()
        return jsonify(card), 200

