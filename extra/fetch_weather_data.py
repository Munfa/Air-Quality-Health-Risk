import pandas as pd
from dotenv import load_dotenv
import requests
import time
import os

load_dotenv()

api_key = os.getenv("openweather_key")

if api_key:
    print("API key loaded securely")

base_url = "https://api.openweathermap.org/data/2.5/weather"
cities = pd.read_csv("cities_metadata.csv")

weather_data = []

for _,row in cities.iterrows():
    params = {
        "lat" : row["lat"],
        "lon" : row["lon"],
        "appid" : api_key,
        "unit" : "metric"
    }

    response = requests.get(base_url, params)
    data = response.json()

    weather_data.append({
        "City" : row["city"],
        "DateTime" : pd.to_datetime(data["dt"], unit='s'),
        "Temperature" : data["main"]["temp"],
        "Pressure" : data["main"]["pressure"],
        "Humidity" : data["main"]["humidity"],
        "wind Speed" : data["wind"]["speed"],
        "Clouds" : data["clouds"]["all"],
        "Weather" : data["weather"][0]["main"] 
    })
    time.sleep(1)

weather_df = pd.DataFrame(weather_data)
weather_df.to_csv("weather_data.csv", index=False)