from pydantic import BaseModel
from datetime import date

class HabitCreate(BaseModel):
    name: str

class HabitResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class RecordCreate(BaseModel):
    date: date


class RecordResponse(BaseModel):
    id: int
    date: date
    habit_id: int

    class Config:
        from_attributes = True
