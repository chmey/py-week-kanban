from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from .config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
if app.env == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)
db = MongoAlchemy(app)
from . import routes # noqa