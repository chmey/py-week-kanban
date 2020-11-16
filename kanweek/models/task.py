from kanweek.extensions import db, ma
from marshmallow import fields


class Task(db.Document):
    id = db.ObjectIdField()
    title = db.StringField()
    description = db.StringField()
    created_date = db.DateTimeField()
    modified_date = db.DateTimeField(required=False)
    labels = db.ListField(db.DocumentField("Label"), required=False)
    weekday = db.DocumentField("Weekday", required=False)


class TaskSchema(ma.Schema):
    id = fields.Str()
    title = fields.Str()
    description = fields.Str()
    created_date = fields.DateTime()

    class Meta:
        fields = ("id", "title", "description", "created_date", "modified_date")
