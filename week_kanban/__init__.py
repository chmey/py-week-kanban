from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate(app, db)


from week_kanban import routes # noqa