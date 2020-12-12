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
    owner = db.ReferenceField('User', required=False)
    completed = db.BooleanField(required=False, default=False)
    archived = db.BooleanField(required=False, default=False)
    dateDue = db.DateTimeField(required=False)


class TaskSchema(ma.Schema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    dateCreated = fields.DateTime()
    dateModified = fields.DateTime()
    weekday = fields.Integer()
    completed = fields.Boolean()
    archived = fields.Boolean()
    dateDue = fields.DateTime()

    class Meta:
        fields = ("id", "title", "description", "dateCreated", "dateModified", "weekday", "completed", "archived", "dateDue")
