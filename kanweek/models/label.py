from kanweek.extensions import db


class Label(db.Document):
    name = db.StringField()
    created_date = db.DateTimeField()
    modified_date = db.DateTimeField()
    user = db.DocumentField("User")
    tasks = db.ListField(db.DocumentField("Task"))
