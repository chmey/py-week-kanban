from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow
from flask_cors import CORS
ma = Marshmallow()
db = MongoEngine()
cors = CORS()
