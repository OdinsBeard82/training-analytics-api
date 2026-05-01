from pydantic import BaseModel
from datetime import date
from fastapi import APIRouter


class WorkoutCreate(BaseModel):
    name: str
    date: date
    duration_minutes: int

class WorkoutRead(BaseModel):
    id: int
    name: str
    date: date
    duration_minutes: int

    model_config = {
        "from_attributes": True
    }
