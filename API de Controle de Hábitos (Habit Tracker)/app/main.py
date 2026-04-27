from fastapi import FastAPI
from .database import engine
from . import models
from .routers import habit, record

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Habit Tracker API")

app.include_router(habit.router)
app.include_router(record.router)
