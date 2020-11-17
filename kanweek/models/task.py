from kanweek.extensions import db, ma
from marshmallow import fields
from datetime import datetime


class Task(db.Document):
    title = db.StringField()
    description = db.StringField(required=False)
    created_date = db.DateTimeField(default=datetime.utcnow())
    modified_date = db.DateTimeField(required=False)
    labels = db.ListField(db.ReferenceField("Label"), required=False)
    weekday = db.IntField(required=False)
    owner = db.ReferenceField('User', required=True)


class TaskSchema(ma.Schema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    created_date = fields.DateTime()
    modified_date = fields.DateTime()

    class Meta:
        fields = ("id", "title", "description", "created_date", "modified_date")
