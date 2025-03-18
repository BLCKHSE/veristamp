from flask import Flask, jsonify, url_for
from flask_cors import CORS
from flask_migrate import Migrate

from .controllers.home import HomeAPI
from .controllers.user import UserAPI
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(f'{__name__.split(".")[0]}.settings')
    CORS(app, origins=app.config.get('CORS_ORIGINS'))
    db.init_app(app)

    with app.app_context():
        from .models.users import user, organisation
        _ = Migrate(app, db)

        register_api(app)

    return app

def register_api(app: Flask):
    url_for('static', filename='img/logo.png')
    home: function = HomeAPI.as_view('home')
    user: function = UserAPI.as_view('users')
    app.add_url_rule('/api/home', view_func=home)
    app.add_url_rule('/api/users', view_func=user)
    app.add_url_rule('/api/users/<int:id>', view_func=user)

app = create_app()

@app.route("/api/health", methods = ["GET", ])
def healthcheck():
    return jsonify({"status": "UP"}), 200
