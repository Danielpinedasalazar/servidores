# app/main.py
from typing import List, Union
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import Item
from .schemas import ItemCreate, ItemOut
from .crud import list_items, create_many_items


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # == reemplaza a @app.on_event("startup") ==
    Base.metadata.create_all(bind=engine)
    yield
    # opcional: lógica de shutdown aquí (cerrar conexiones, limpiar, etc.)


app = FastAPI(title="Items API", version="1.0.0", lifespan=lifespan)


@app.get("/items", response_model=List[ItemOut], summary="Listar items")
def get_items(db: Session = Depends(get_db)):
    return list_items(db)


@app.post("/items", response_model=List[ItemOut], summary="Crear 1 o varios items")
def create_items(
    body: Union[ItemCreate, List[ItemCreate]],
    db: Session = Depends(get_db),
):
    payloads = body if isinstance(body, list) else [body]
    return create_many_items(db, payloads)
