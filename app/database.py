import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Permite sobreescribir por variable de entorno. Ej: sqlite:////data/items.db en Docker
DATABASE_URL = os.getenv("DB_URL", "sqlite:///./items.db")

# Para SQLite se recomienda check_same_thread=False con SQLAlchemy 2.x (modo clásico)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

Base = declarative_base()
