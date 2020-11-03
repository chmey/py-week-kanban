from sqlalchemy import Model, Column, Integer, String, DateTime, relationship
from datetime import datetime


class User(Model):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(), index=True)
    email = Column(String(), index=True, unique=True)
    _pwhash = Column(String(128))
    join_date = Column(DateTime())
    modified_date = Column(DateTime(), nullable=True)
    labels = relationship("Label", back_populates="user")

    def __init__(self):
        self.join_date = datetime.now()
