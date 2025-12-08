from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# point to database
DATABASE_URL = "sqlite:///./dummy_database.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} # needed for SQLite + FastAPI
    )

# each request will use a sessionlocal instance to talk to the db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class that our models will inherit from
Base = declarative_base()

# dependency for fastAPI routes: get a DB session and close it after the request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()