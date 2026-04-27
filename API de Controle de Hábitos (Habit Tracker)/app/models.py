from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    records = relationship("HabitRecord", back_populates="habit")


class HabitRecord(Base):
    __tablename__ = "habit_records"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)

    habit_id = Column(Integer, ForeignKey("habits.id"))

    habit = relationship("Habit", back_populates="records")
