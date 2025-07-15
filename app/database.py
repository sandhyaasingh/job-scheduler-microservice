from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# For local demo, we'll use SQLite (Postgres is optional for now)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jobs.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# DB init on app startup
def create_db():
    from app.models import job  # import here to avoid circular import
    Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
