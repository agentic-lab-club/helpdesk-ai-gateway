from pydantic import BaseModel
from app.models.employee import EmployeeStatus


class EmployeeRead(BaseModel):
    id: int
    telegram_id: str
    telegram_username: str | None
    full_name: str
    status: EmployeeStatus

    class Config:
        from_attributes = True
