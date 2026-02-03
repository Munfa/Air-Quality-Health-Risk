import numpy as np
import pandas as pd

# Breakpoints for PM2.5 (µg/m³)
PM25_BREAKPOINTS = [
    (0.0, 12.0, 0, 50),
    (12.1, 35.4, 51, 100),
    (35.5, 55.4, 101, 150),
    (55.5, 150.4, 151, 200),
    (150.5, 250.4, 201, 300),
    (250.5, 500.4, 301, 500)
]

# Breakpoints for PM10 (µg/m³)
PM10_BREAKPOINTS = [
    (0, 54, 0, 50),
    (55, 154, 51, 100),
    (155, 254, 101, 150),
    (255, 354, 151, 200),
    (355, 424, 201, 300),
    (425, 604, 301, 400)
]

# Breakpoints for NO2 (ppb)
NO2_BREAKPOINTS = [
    (0, 53, 0, 50),
    (54, 100, 51, 100),
    (101, 360, 101, 150),
    (361, 649, 151, 200),
    (650, 1249, 201, 300),
    (1250, 2049, 301, 400)
]

# Breakpoints for CO (ppm)
CO_BREAKPOINTS = [
    (0.0, 4.4, 0, 50),
    (4.5, 9.4, 51, 100),
    (9.5, 12.4, 101, 150),
    (12.5, 15.4, 151, 200),
    (15.5, 30.4, 201, 300),
    (30.5, 50.4, 301, 400)
]

# Breakpoints for O3 (ppm)
O3_BREAKPOINTS = [
    (0.000, 0.054, 0, 50),
    (0.055, 0.070, 51, 100),
    (0.071, 0.085, 101, 150),
    (0.086, 0.105, 151, 200),
    (0.106, 0.200, 201, 300)
]

# Breakpoints for SO2 (ppb)
SO2_BREAKPOINTS = [
    (0, 35, 0, 50),
    (36, 75, 51, 100),
    (76, 185, 101, 150),
    (186, 304, 151, 200),
    (305, 604, 201, 300),
    (605, 1004, 301, 500)
]

'''
    AQI calculation formula where, 

    Cp = the concentration of the pollutant
    I_high = the AQI value corresponding to the high breakpoint
    I_low = the AQI value corresponding to the low breakpoint
    Bp_high = the breakpoint concentration that is greater than Cp
    Bp_low = the breakpoint concentration that is less than Cp
'''
def calculate_aqi(Cp, breakpoints):
    for Bp_low, Bp_high, I_low, I_high in breakpoints:
        if Bp_low <= Cp <= Bp_high:
            aqi_value = ((I_high - I_low)/(Bp_high - Bp_low)) * (Cp - Bp_low) + I_low
            return aqi_value
    return np.nan
    
def compute_aqi_per_row(row):
    pm25 = row.get("PM2.5")
    pm10 = row.get("PM10")
    no2 = row.get("NO2")
    so2 = row.get("SO2")
    co = row.get("CO")
    o3 = row.get("O3")

    aqi_values = []
    if pd.notna(pm25):
        aqi_values.append(calculate_aqi(pm25, PM25_BREAKPOINTS))
    if pd.notna(pm10):
        aqi_values.append(calculate_aqi(pm10, PM10_BREAKPOINTS))
    if pd.notna(no2):
        aqi_values.append(calculate_aqi(no2, NO2_BREAKPOINTS))
    if pd.notna(so2):
        aqi_values.append(calculate_aqi(so2, SO2_BREAKPOINTS))
    if pd.notna(co):
        aqi_values.append(calculate_aqi(co, CO_BREAKPOINTS))
    if pd.notna(o3):
        aqi_values.append(calculate_aqi(o3, O3_BREAKPOINTS))

    if len(aqi_values) == 0:
        return np.nan
    
    return round(max(aqi_values), 2)

def compute_aqi(df):
    df['AQI'] = df.apply(compute_aqi_per_row, axis=1)
    return df

def assess_health_risk(aqi, weather_data):
    ##### Assess health risk #####
    if aqi <= 50:
        risk = "Good"
    elif aqi <= 100:
        risk = "Moderate"
    elif aqi <= 150:
        risk = "Unhealthy for Sensitive Groups"     
    elif aqi <= 200:
        risk = "Unhealthy"
    elif aqi <= 300:
        risk = "Very Unhealthy"
    else:
        risk = "Hazardous"
    

    return risk