from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(
        DateTime(timezone=False), nullable=False, server_default=func.now()
    )
