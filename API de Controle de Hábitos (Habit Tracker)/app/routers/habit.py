from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/habits", tags=["Habits"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.HabitResponse)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    return crud.create_habit(db, habit)

@router.get("/", response_model=list[schemas.HabitResponse])
def list_habits(db: Session = Depends(get_db)):
    return crud.get_habits(db)

@router.put("/{habit_id}")
def update_habit(habit_id: int, habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    return crud.update_habit(db, habit_id, habit)

@router.delete("/{habit_id}")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    return crud.delete_habit(db, habit_id)
