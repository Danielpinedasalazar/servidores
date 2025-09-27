from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, description="Precio > 0")
    # Lo puedes enviar o no; si no viene, el server pone NOW()
    created_at: Optional[datetime] = None


class ItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # permite mapear desde ORM
    id: int
    name: str
    price: float
    created_at: datetime
