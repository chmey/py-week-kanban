from kanweek.extensions import db, ma
from marshmallow import fields
from datetime import datetime


class Task(db.Document):
    title = db.StringField()
    description = db.StringField(required=False)
    dateCreated = db.DateTimeField(default=datetime.utcnow())
    dateModified = db.DateTimeField(required=False)
    labels = db.ListField(db.ReferenceField("Label"), required=False)
    weekday = db.IntField(required=False)
    owner = db.ReferenceField('User', required=True)


class TaskSchema(ma.Schema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    dateCreated = fields.DateTime()
    dateModified = fields.DateTime()

    class Meta:
        fields = ("id", "title", "description", "dateCreated", "dateModified")
