from flask import Flask
from .config import DevelopmentConfig, ProductionConfig


def create_app():
    app = Flask(__name__)
    if app.env == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from .api import bpAPI
    from .frontend import bpFrontend

    app.register_blueprint(bpAPI)
    app.register_blueprint(bpFrontend)


def register_extensions(app):
    from .extensions import db, ma

    db.init_app(app)
    ma.init_app(app)


app = create_app()
