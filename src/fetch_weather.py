
import requests
import time
import os

base_url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(lat, lon, api_key):

    params = {
        "lat" : lat,
        "lon" : lon,
        "appid" : api_key,
        "unit" : "metric"
    }

    response = requests.get(base_url, params)
    data = response.json()

    return{
        "Temperature" : data["main"]["temp"],
        "Humidity" : data["main"]["humidity"],
        "Wind Speed" : data["wind"]["speed"]
    }