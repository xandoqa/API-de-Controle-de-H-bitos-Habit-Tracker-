from sqlalchemy.orm import Session
from . import models, schemas

def create_habit(db: Session, habit: schemas.HabitCreate):
    db_habit = models.Habit(name=habit.name)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

def get_habits(db: Session):
    return db.query(models.Habit).all()

def update_habit(db: Session, habit_id: int, habit: schemas.HabitCreate):
    db_habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    if db_habit:
        db_habit.name = habit.name
        db.commit()
        db.refresh(db_habit)
    return db_habit

def delete_habit(db: Session, habit_id: int):
    db_habit = db.query(models.Habit).filter(models.Habit.id == habit_id).first()
    if db_habit:
        db.delete(db_habit)
        db.commit()
    return {"message": "Deleted"}

def add_record(db: Session, habit_id: int, record: schemas.RecordCreate):
    db_record = models.HabitRecord(habit_id=habit_id, date=record.date)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_records(db: Session, habit_id: int):
    return db.query(models.HabitRecord).filter(
        models.HabitRecord.habit_id == habit_id
    ).all()
