from flask import Flask, jsonify, url_for
from flask_cors import CORS
from flask_migrate import Migrate

from .controllers import (
    HomeAPI,
    StampAddonApi,
    SubscriptionAPI,
    TemplateApi,
    TemplateAddonAPI,
    TemplateStampApi,
    UserAPI
)
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(f'{__name__.split(".")[0]}.settings')
    CORS(app, origins=app.config.get('CORS_ORIGINS'))
    db.init_app(app)

    with app.app_context():
        from .models import documents, user, organisation, stamps, subscriptions
        _ = Migrate(app, db)

        register_api(app)

    return app

def register_api(app: Flask):
    url_for('static', filename='img/logo.png')
    user: function = UserAPI.as_view('users')
    app.add_url_rule('/api/home', view_func=HomeAPI.as_view('home'))
    app.add_url_rule('/api/users', view_func=user)
    app.add_url_rule('/api/users/<int:id>', view_func=user)
    app.add_url_rule('/api/payments/<string:provider>', view_func=SubscriptionAPI.as_view('subscriptions'))
    app.add_url_rule('/api/addon/templates', view_func=TemplateAddonAPI.as_view('addon_templates'))
    app.add_url_rule('/api/templates', view_func=TemplateApi.as_view('templates'))
    app.add_url_rule('/api/addon/templates/stamps', view_func=TemplateStampApi.as_view('stamp_templates'))
    app.add_url_rule('/api/addon/stamps', view_func=StampAddonApi.as_view('stamps'))

app = create_app()

@app.route("/api/health", methods = ["GET", ])
def healthcheck():
    return jsonify({"status": "UP"}), 200
