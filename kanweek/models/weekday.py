from sqlalchemy import Model, Column, Integer, String, relationship


class Weekday(Model):
    __tablename__ = 'weekday'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    tasks = relationship("Task", back_populates="weekday")
