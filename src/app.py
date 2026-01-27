import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from features import assess_health_risk

app = FastAPI()

data = {
    'PM2.5' : 86.57,
    'PM10' : 25.19,
    'NO2' : 99.88,
    'SO2' : 30.63,
    'CO' : 4.46,
    'O3' : 36.29,
    'Temperature' : 17.67,
    'Humidity' : 59.35,
    'Wind Speed' : 13.76
}

model = joblib.load("saved_models/model.joblib")
scaler = joblib.load("saved_models/scaler.joblib")

keys_to_select = ["Temperature", "Humidity", "Wind Speed"]
weather_data = {k : data[k] for k in keys_to_select if k in data}

df = pd.DataFrame([data])
scaled_df = scaler.transform(df)
aqi = model.predict(scaled_df)
# aqi = round(aqi, 2)

result = assess_health_risk(aqi, weather_data)

print(aqi)
print(result)