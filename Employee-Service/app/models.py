import uuid
from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import enum


class EmployeeStatus(str, enum.Enum):
    FREE = "FREE"      # свободен
    BUSY = "BUSY"      # не свободен


class Employee(Base):
    __tablename__ = "employees"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )
    full_name = Column(String(255), nullable=False)
    telegram_id = Column(String(100), nullable=False, unique=True, index=True)
    status = Column(
        Enum(EmployeeStatus, name="employee_status"),
        nullable=False,
        default=EmployeeStatus.FREE,
    )
