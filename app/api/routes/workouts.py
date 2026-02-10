from fastapi import APIRouter, Depends
from app.db.session import get_db

router = APIRouter()

@router.get("/workouts")
def get_workouts():
    return {"status": "ok"}
