from kanweek.extensions import db, ma
from marshmallow import fields
from datetime import datetime


class Label(db.Document):
    name = db.StringField(required=True)
    dateModified = db.DateTimeField(required=False, default=datetime.utcnow())
    owner = db.ReferenceField("User")
    tasks = db.ListField(db.ReferenceField("Task"))


class LabelSchema(ma.Schema):
    id = fields.Str()
    name = fields.Str()
    dateModified = fields.DateTime()

    class Meta:
        fields = ("id", "name", "dateModified")
