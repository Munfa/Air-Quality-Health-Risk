import streamlit as st 
import requests
import pandas as pd

cities = ['Dhaka', 'Delhi', 'Mumbai', 'Beijing', 'London', 
            'Paris', 'New York', 'Los Angeles', 'Tokyo', 'Seoul', 
            'Bangkok', 'Sydney']

st.title("Air Quality & Health Risk Prediction")

selected_city = st.selectbox("Select a City", cities)

if st.button("Predict AQI"):
    response = requests.get(
        f"https://air-quality-health-risk.onrender.com/predict/{selected_city}"
    )
    
    if response.status_code == 200:
        result = response.json()

        st.success(f"City: {result["city"]}")
        st.write("Predicted AQI: ", result["predicted_aqi"])
        st.write("Health Risk: ", result["health_risk"])

    else: 
        st.error("Prediction Failed!!")

    if selected_city:
        response = requests.get(
            f"https://air-quality-health-risk.onrender.com/history/{selected_city}"
        )
        if response.status_code == 200:
            data = response.json()

            if len(data) == 0:
                st.warning("No AQI data available yet!")

            else:    
                df = pd.DataFrame(data)
                df["date"] = pd.to_datetime(df["datetime"]).dt.date

            st.line_chart(
                df.set_index("date")["aqi"]
            )