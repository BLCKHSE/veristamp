import os
from dotenv import load_dotenv
from flask import Flask, jsonify

def create_app(env: str = 'development'):
    ENV_MAPPER = {'development': '.env', 'production': '.env', 'testing' : '.testing.env'}
    load_dotenv(ENV_MAPPER.setdefault(env, '.env'))
    app = Flask(__name__)
    app.config.update(
        TESTING = os.getenv('TESTING'),
    )

    return app

def register_api(app: Flask, name: str):
    pass

app = create_app()

@app.route("/health", methods = ["GET", ])
def hello_world():
    return jsonify({"status": "UP"}), 200
