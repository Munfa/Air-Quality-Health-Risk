import pandas as pd
import numpy as np
import requests
import os
from dotenv import load_dotenv

load_dotenv()


openaq_key = os.getenv("openaq_key")

if openaq_key:
    print("API key loaded securely")


base_location = "https://api.openaq.org/v3/locations"
# base_measurements = "https://api.openaq.org/v3/measurements"
headers = {
       'X-API-Key' : openaq_key
}
all_data = []
cities = pd.read_csv("cities_metadata.csv")

for _,row in cities.iterrows():
    city = row["city"]
    
    loc_res = requests.get(
        base_location,
        headers = headers,
        params = {'city' : city, 'limit' : 5, 'sort' : 'desc'}
    )
    # print(loc_res.status_code)
    # print(loc_res.text)
    locations = loc_res.json()["results"]
    # loc_ids = [loc["id"] for loc in locations]
    # print(loc_ids)
    # print(locations)
    # print(locations['id'])
    for loc in locations:
        location_id = loc["id"]
        base_measurements = f"https://api.openaq.org/v3/locations/{location_id}/latest"
        params = {
            'location_id' : loc["id"],
            'parameter' : ['pm25', 'pm10'],
            "date_from": "2023-01-01",
            "date_to": "2025-31-31",
            "limit": 100
        }
    #     params = {
    #         'limit' : 300,
    #         'page' : 3
    #     }

        response = requests.get(base_measurements, params=params, headers=headers)
        if response.status_code != 200:
            continue
        else:
            print(response.status_code)
            print(response.text)
        
#         data = response.json().get("results", [])
#         all_data.extend(data)
    

# print(all_data[:5])