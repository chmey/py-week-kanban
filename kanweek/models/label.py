from mongoalchemy import Document, StringField, ReferenceField, ListField, DateTimeField
from datetime import datetime
from .user import User
from .task import Task


class Label(Document):
    name = StringField()
    created_date = DateTimeField()
    modified_date = DateTimeField()
    user = ReferenceField(User)
    tasks = ListField(ReferenceField(Task))

    def __init__(self):
        self.created_date = datetime.now()
