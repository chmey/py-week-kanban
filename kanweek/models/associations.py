from sqlalchemy import Table, Base, Integer, ForeignKey, Column

tasks_labels = Table(
    'tasks_labels', Base.metadata,
    Column('task_id', Integer, ForeignKey('task.id')),
    Column('label_id', Integer, ForeignKey('label.id'))
)
