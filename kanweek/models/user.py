from kanweek.extensions import db, ma
from datetime import datetime


class User(db.Document):
    username = db.StringField()
    email = db.StringField()
    _pwhash = db.StringField(max_length=128)
    join_date = db.DateTimeField()
    modified_date = db.DateTimeField()
    labels = db.ListField(db.DocumentField("Label"))

    def __init__(self):
        self.join_date = datetime.now()


class UserSchema(ma.Schema):
    class Meta:
        fields = ("username", "email", "join_date")
