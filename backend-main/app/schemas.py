from uuid import UUID
from pydantic import BaseModel, Field
from typing import Optional
from app.models import EmployeeStatus


class EmployeeBase(BaseModel):
    full_name: str = Field(..., max_length=255)
    telegram_id: str = Field(..., max_length=100)


class EmployeeCreate(EmployeeBase):
    status: Optional[EmployeeStatus] = EmployeeStatus.FREE


class EmployeeUpdate(BaseModel):
    full_name: Optional[str] = Field(None, max_length=255)
    telegram_id: Optional[str] = Field(None, max_length=100)
    status: Optional[EmployeeStatus] = None


class EmployeeUpdateStatus(BaseModel):
    status: EmployeeStatus


class EmployeeTelegramId(BaseModel):
    telegram_id: str


class EmployeeRead(EmployeeBase):
    id: UUID
    status: EmployeeStatus

    class Config:
        from_attributes = True
