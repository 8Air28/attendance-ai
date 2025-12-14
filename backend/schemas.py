from pydantic import BaseModel

class AttendanceBase(BaseModel):
    date: str
    start_time: str
    end_time: str
    note: str | None = None

class AttendanceCreate(AttendanceBase):
    pass

class Attendance(AttendanceBase):
    id: int

    class Config:
        orm_mode = True
