from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.workout import create_workout, get_workout_by_id
from app.schemas.workout import WorkoutCreate, WorkoutRead

router = APIRouter()

@router.get("/workouts/{workout_id}", response_model=WorkoutRead)
def get_workout(workout_id: int, db: Session = Depends(get_db)):
    workout = get_workout_by_id(db, workout_id)
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout

@router.post("/workouts", response_model=WorkoutRead)
def create(workout: WorkoutCreate, db: Session = Depends(get_db)):
    return create_workout(db, workout)