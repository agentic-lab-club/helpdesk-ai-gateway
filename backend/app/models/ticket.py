from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.configs.database import Base
import enum


class TicketStatus(str, enum.Enum):
    OPEN = "В работе"
    CLOSED = "Закрыто"
    UNSOLVED = "Не решено"


class TicketLevel(int, enum.Enum):
    FIRST_LINE = 1
    SECOND_LINE = 2


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    priority_id = Column(Integer, ForeignKey("priorities.id"), nullable=False)
    
    message = Column(Text, nullable=False)
    email = Column(String(255), nullable=False)
    level_key = Column(
        Enum(TicketLevel, name="ticket_level"),
        nullable=False,
        default=TicketLevel.FIRST_LINE,
    )
    status = Column(
        Enum(TicketStatus, name="ticket_status"),
        nullable=False,
        default=TicketStatus.OPEN,
    )
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Связи
    employee = relationship("Employee", back_populates="tickets")
    category = relationship("Category", back_populates="tickets")
    priority = relationship("Priority", back_populates="tickets")
    chat_history = relationship("ChatHistory", back_populates="ticket")
