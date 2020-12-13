from kanweek.extensions import db, ma
from marshmallow import fields
from datetime import datetime
from passlib.apps import custom_app_context as pwd_hash


class User(db.Document):
    username = db.StringField()
    email = db.StringField(required=True)
    _pwhash = db.StringField(max_length=128, required=True)
    dateJoined = db.DateTimeField(default=datetime.utcnow())
    dateModified = db.DateTimeField()
    labels = db.ListField(db.ReferenceField("Label"), required=False)
    disabled = db.BooleanField(required=False, default=False)

    def verify_password(self, check_pw_against):
        return pwd_hash.verify(check_pw_against, self._pwhash)

    def set_password_hash(self, pw_to_hash):
        self._pwhash = pwd_hash.encrypt(pw_to_hash)


class UserSchema(ma.Schema):
    id = fields.Str()
    username = fields.Str()
    dateJoined = fields.DateTime()
    email = fields.Str()
    disabled = fields.Boolean()

    class Meta:
        fields = ("id", "username", "email", "dateJoined", "disabled")
