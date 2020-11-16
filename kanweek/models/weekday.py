from mongoalchemy import Document, StringField, ReferenceField, ListField
from .task import Task


class Weekday(Document):
    __tablename__ = 'weekday'
    name = StringField()
    tasks = ListField(ReferenceField(Task))
