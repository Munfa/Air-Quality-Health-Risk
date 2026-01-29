import pandas as pd
from dotenv import load_dotenv
import requests
import time
import os

base_url = "https://api.openweathermap.org/data/2.5/weather"

# weather_data = []

def get_weather(lat, lon, api_key):

# for _,row in cities.iterrows():
    params = {
        "lat" : lat,
        "lon" : lon,
        "appid" : api_key,
        "unit" : "metric"
    }

    response = requests.get(base_url, params)
    data = response.json()

    return{
        # "DateTime" : pd.to_datetime(data["dt"], unit='s'),
        "Temperature" : data["main"]["temp"],
        "Humidity" : data["main"]["humidity"],
        "wind Speed" : data["wind"]["speed"]
    }
    # time.sleep(1)

# weather_df = pd.DataFrame(weather_data)