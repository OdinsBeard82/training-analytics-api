from pydantic import BaseModel
from datetime import date

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

