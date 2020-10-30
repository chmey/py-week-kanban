from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), index=True)
    email = db.Column(db.String(), index=True, unique=True)
    _pwhash = db.Column(db.String(128))
    join_date = db.Column(db.DateTime())
    modified_date = db.Column(db.DateTime(), nullable=True)
    labels = db.relationship("Label", back_populates="user")

    def __init__(self):
        self.join_date = datetime.now()


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=True)
    description = db.Column(db.String(), nullable=True)
    created_date = db.Column(db.DateTime())
    modified_date = db.Column(db.DateTime(), nullable=True)
    labels = relationship("Label", secondary=association_table)
    weekday_id = db.Column(db.Integer(), db.ForeignKey('weekday.id'))


    def __init__(self):
        self.created_date = datetime.now()
        

class Label(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    created_date = db.Column(db.DateTime())
    modified_date = db.Column(db.DateTime(), nullable=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))  # TODO: Can Label only belong to one user?
    tasks = relationship("Task", secondary=association_table)

    def __init__(self):
        self.created_date = datetime.now()


association_table = db.Table('tasks_labels', db.Base.metadata,
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('label_id', db.Integer, db.ForeignKey('label.id'))
)


class Weekday(db.Model):
    __tablename__ = 'weekday'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    tasks = relationship("Task", back_populates="weekday")

    def __init__(self):
        self.created_date = datetime.now()
