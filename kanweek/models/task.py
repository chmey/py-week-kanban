from kanweek.extensions import db
from datetime import datetime


class Task(db.Document):
    title = db.StringField()
    description = db.StringField()
    created_date = db.DateTimeField()
    modified_date = db.DateTimeField()
    labels = db.ListField(db.DocumentField("Label"))
    weekday = db.DocumentField("Weekday")

    def __init__(self):
        self.created_date = datetime.now()
