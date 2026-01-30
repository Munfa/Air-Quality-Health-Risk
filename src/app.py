import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
from src.features import assess_health_risk
from src.fetch_weather import get_weather
from src.fetch_air_pollutant import get_pollutant

app = FastAPI()
model = joblib.load("saved_models/model.joblib")
scaler = joblib.load("saved_models/scaler.joblib")

load_dotenv()
api_key = os.getenv("openweather_key")
cities = pd.read_csv("data/cities_metadata.csv")

def get_coordinates(city):
    row = cities[cities["city"] == city]
    if row.empty:
        return None
    return (row["lat"], row["lon"])

@app.get("/")
def home():
    return {"AQI Health Risk Assessment System is Running"}

@app.get("/predict/{city}")
def predict_city_aqi(city: str):
    coords = get_coordinates(city)

    if coords is None:
        return {"Error": "City not found"}
    lat, lon = coords

    pollutant_data = get_pollutant(lat, lon, api_key)
    weather_data = get_weather(lat, lon, api_key)

    data = {**pollutant_data, **weather_data}
        
    df = pd.DataFrame([data])
    scaled_df = scaler.transform(df)
    aqi = model.predict(scaled_df)[0]

    risk = assess_health_risk(aqi, weather_data)

    return {
        "city" : city,
        "predicted_aqi" : round(float(aqi), 2),
        "health_risk" : risk
    }

