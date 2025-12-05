from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.configs.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    cat_key = Column(String(50), nullable=False, unique=True, index=True)  # web, voip, vpn
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    # Связь с заявками
    tickets = relationship("Ticket", back_populates="category")
