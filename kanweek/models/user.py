from mongoalchemy import Document, StringField, ReferenceField, ListField, DateTimeField
from datetime import datetime
from .label import Label


class User(Document):
    username = StringField()
    email = StringField(unique=True)
    _pwhash = StringField(max_length=128)
    join_date = DateTimeField()
    modified_date = DateTimeField()
    labels = ListField(ReferenceField(Label))

    def __init__(self):
        self.join_date = datetime.now()
