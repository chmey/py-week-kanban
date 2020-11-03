from sqlalchemy import Model, Column, Integer, String, DateTime, ForeignKey, relationship
from datetime import datetime
from .associations import tasks_labels


class Task(Model):
    __tablename__ = 'task'
    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=True)
    description = Column(String(), nullable=True)
    created_date = Column(DateTime())
    modified_date = Column(DateTime(), nullable=True)
    labels = relationship("Label", secondary=tasks_labels)
    weekday_id = Column(Integer(), ForeignKey('weekday.id'))

    def __init__(self):
        self.created_date = datetime.now()
