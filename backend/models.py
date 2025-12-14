from sqlalchemy import Column, Integer, String
from .database import Base

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    start_time = Column(String)
    end_time = Column(String)
    note = Column(String, nullable=True)
