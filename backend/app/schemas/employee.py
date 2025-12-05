from pydantic import BaseModel
from typing import Optional
from app.models.employee import EmployeeStatus


class EmployeeBase(BaseModel):
    telegram_id: str
    telegram_username: Optional[str] = None
    full_name: str


class EmployeeCreate(EmployeeBase):
    status: Optional[EmployeeStatus] = EmployeeStatus.FREE


class EmployeeUpdate(BaseModel):
    telegram_id: Optional[str] = None
    telegram_username: Optional[str] = None
    full_name: Optional[str] = None
    status: Optional[EmployeeStatus] = None


class EmployeeRead(EmployeeBase):
    id: int
    status: EmployeeStatus

    class Config:
        from_attributes = True
