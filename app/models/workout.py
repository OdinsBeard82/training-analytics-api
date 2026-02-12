from sqlalchemy import Column, Integer, String, Date, CheckConstraint
from app.db.base import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    duration_minutes = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint('duration_minutes > 0 and duration_minutes < 60'),
    )

