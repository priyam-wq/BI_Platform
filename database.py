import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from the environment
MYSQL_URL = os.getenv("MYSQL_URL")

# Create the SQLAlchemy engine
# Note: echo=True is helpful for debugging to see the generated SQL
engine = create_engine(MYSQL_URL, echo=False)

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency for FastAPI to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
