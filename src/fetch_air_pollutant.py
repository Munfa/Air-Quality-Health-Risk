import pandas as pd
import numpy as np
import requests

base_url = "https://api.openweathermap.org/data/2.5/air_pollution"

def get_pollutant(lat, lon, api_key):
    params = {
        "lat" : lat,
        "lon" : lon,
        "appid" : api_key,
    }

    response = requests.get(base_url, params)
    data = response.json()
    components = data["list"][0]["components"]

    return{
        "PM2.5": components["pm2_5"],
        "PM10": components["pm10"],
        "NO2": components["no2"],
        "SO2": components["so2"],
        "CO": components["co"],
        "O3": components["o3"]
    }