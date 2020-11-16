from .common import bpAPI
from kanweek.models.user import UserSchema
from kanweek.extensions import db
siSchema = UserSchema()
plSchema = UserSchema(many=True)
