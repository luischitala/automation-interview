from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
db_host = os.getenv('POSTGRES_HOST', 'postgres')
db_port = os.getenv('POSTGRES_PORT', '5432')
db_name = os.getenv('POSTGRES_DB', 'mydatabase')
db_user = os.getenv('POSTGRES_USER', 'mydbuser')
db_password = os.getenv('POSTGRES_PASSWORD', 'mydbpassword')

# SQLAlchemy configurations
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define the Extraction model
class Extraction(Base):
    __tablename__ = "Extractions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    content = Column(JSON)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Perform actions during app startup
    # For example, create database tables if they don't exist
    Base.metadata.create_all(bind=engine, checkfirst=True)

@app.on_event("shutdown")
def shutdown_event():
    # Perform actions during app shutdown
    pass

@app.get("/")
def read_root():
    return {"message": "Hello, this is the FastAPI app!"}
