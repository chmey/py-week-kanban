from kanweek.extensions import db


class Weekday(db.Document):
    __tablename__ = 'weekday'
    name = db.StringField()
    tasks = db.ListField(db.DocumentField("Task"))
