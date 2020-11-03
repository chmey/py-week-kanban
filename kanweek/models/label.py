from sqlalchemy import Model, Column, String, DateTime, Integer, ForeignKey, relationship
from datetime import datetime
from .associations import tasks_labels


class Label(Model):
    __tablename__ = 'label'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    created_date = Column(DateTime())
    modified_date = Column(DateTime(), nullable=True)
    user_id = Column(Integer(), ForeignKey('user.id'))  # TODO: Can Label only belong to one user?
    tasks = relationship("Task", secondary=tasks_labels)

    def __init__(self):
        self.created_date = datetime.now()
