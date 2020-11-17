from kanweek.extensions import db, ma


class User(db.Document):
    username = db.StringField()
    email = db.StringField(required=True)
    _pwhash = db.StringField(max_length=128)
    dateJoined = db.DateTimeField()
    dateModified = db.DateTimeField()
    labels = db.ListField(db.ReferenceField("Label"))


class UserSchema(ma.Schema):
    class Meta:
        fields = ("username", "email", "dateJoined")
