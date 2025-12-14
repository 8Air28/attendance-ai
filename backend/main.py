from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal
from .services.report_service import generate_monthly_report
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from fastapi import Query

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/attendances")
def read_attendance(db: Session = Depends(get_db)):
    return db.query(models.Attendance).all()

@app.post("/attendances")
def create_attendance(item: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    data = models.Attendance(**item.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@app.post("/report")
def report(month: str, db: Session = Depends(get_db)):
    items = db.query(models.Attendance).filter(
        models.Attendance.date.like(f"{month}-%")
    ).all()

    if not items:
        return {"report": "この月の勤怠データはありません。"}

    dicts = [
        {
            "date": i.date,
            "start_time": i.start_time,
            "end_time": i.end_time,
            "note": i.note,
        }
        for i in items
    ]

    summary = generate_monthly_report(dicts)
    return {"report": summary}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
