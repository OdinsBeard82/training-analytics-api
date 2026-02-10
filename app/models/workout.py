from sqlalchemy import Column, Integer
from app.db.base import Base

class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True)
