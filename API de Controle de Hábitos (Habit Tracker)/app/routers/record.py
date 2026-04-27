from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter(prefix="/records", tags=["Records"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{habit_id}", response_model=schemas.RecordResponse)
def add_record(habit_id: int, record: schemas.RecordCreate, db: Session = Depends(get_db)):
    return crud.add_record(db, habit_id, record)

@router.get("/{habit_id}", response_model=list[schemas.RecordResponse])
def list_records(habit_id: int, db: Session = Depends(get_db)):
    return crud.get_records(db, habit_id)
