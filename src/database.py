import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

database_url = os.getenv("database_url")
engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class AQIPrediction(Base):
    __tablename__ = "aqi_predictions"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    predicted_aqi = Column(Float)
    health_risk = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

