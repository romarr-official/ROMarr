from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


# Default to local SQLite under /app/data (overridden in Docker)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/romarr.db")


connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Called at startup to create tables if missing
def init_db():
    from .models import Rom
    Base.metadata.create_all(bind=engine)