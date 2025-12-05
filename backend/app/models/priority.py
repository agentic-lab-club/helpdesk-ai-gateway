from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.configs.database import Base


class Priority(Base):
    __tablename__ = "priorities"

    id = Column(Integer, primary_key=True, index=True)
    pri_key = Column(Integer, nullable=False, unique=True, index=True)  # 1, 2, 3
    name = Column(String(50), nullable=False)  # Низкий, Средний, Высокий
    description = Column(String(255), nullable=True)

    # Связь с заявками
    tickets = relationship("Ticket", back_populates="priority")
