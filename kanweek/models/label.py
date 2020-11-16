from kanweek.extensions import db
from datetime import datetime


class Label(db.Document):
    name = db.StringField()
    created_date = db.DateTimeField()
    modified_date = db.DateTimeField()
    user = db.DocumentField("User")
    tasks = db.ListField(db.DocumentField("Task"))

    def __init__(self):
        self.created_date = datetime.now()
