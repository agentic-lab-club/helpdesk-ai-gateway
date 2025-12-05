from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.configs.database import Base
import enum


class EmployeeStatus(str, enum.Enum):
    FREE = "Свободен"
    BUSY = "Не Свободен"


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String(100), nullable=False, unique=True, index=True)
    telegram_username = Column(String(100), nullable=True)
    full_name = Column(String(255), nullable=False)
    status = Column(
        Enum(EmployeeStatus, name="employee_status"),
        nullable=False,
        default=EmployeeStatus.FREE,
    )

    # Связь с заявками
    tickets = relationship("Ticket", back_populates="employee")
