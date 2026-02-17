from app.models.workout import Workout
from app.schemas.workout import WorkoutCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


def create_workout(db: Session, workout: WorkoutCreate):
    db_workout = Workout(**workout.model_dump())
    db.add(db_workout)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="commit failed")

    db.refresh(db_workout)
    return db_workout


def get_workout_by_id(db: Session, workout_id: int):
    return db.get(Workout, workout_id)

