from mongoalchemy import Document, StringField, ReferenceField, ListField, DateTimeField
from datetime import datetime
from .weekday import Weekday
from .label import Label


class Task(Document):
    title = StringField()
    description = StringField()
    created_date = DateTimeField()
    modified_date = DateTimeField()
    labels = ListField(ReferenceField(Label))
    weekday = ReferenceField(Weekday)

    def __init__(self):
        self.created_date = datetime.now()
