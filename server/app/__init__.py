from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from app.views import ViewInsert
from app.models import ModelInsert
from app.docs import TEMPLATE

from config.dev import DevConfig
from config.production import ProductionConfig


def create_app(dev=True):
    app_ = Flask(__name__)
    app_.config.from_object(DevConfig if dev else ProductionConfig)

    JWTManager().init_app(app_)
    CORS(app_)
    Swagger(template=TEMPLATE).init_app(app_)

    ViewInsert(app_)
    ModelInsert(app_)

    return app_


app = create_app()


@app.after_request
def set_security_header(response):
    response.headers['X-Content-Type-Options'] = 'nosiff'
    response.headers['X-Frames-Options'] = 'deny'

    return response
