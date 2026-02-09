from app.db.base import Base
from sqlalchemy import Column, Integer


class TableName(Base):
    __tablename__ = "workout"
    id = Column(Integer, primary_key=True)
