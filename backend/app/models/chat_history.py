from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.configs.database import Base
import enum


class SenderType(str, enum.Enum):
    USER = "user"
    EMPLOYEE = "employee"
    AI = "ai"


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    
    message = Column(Text, nullable=False)
    sender_type = Column(
        Enum(SenderType, name="sender_type"),
        nullable=False,
    )
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    # Связь с заявкой
    ticket = relationship("Ticket", back_populates="chat_history")
