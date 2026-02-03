import streamlit as st 
import requests

cities = ['Dhaka', 'Delhi', 'Mumbai', 'Beijing', 'London', 
            'Paris', 'New York', 'Los Angeles', 'Tokyo', 'Seoul', 
            'Bangkok', 'Sydney']

st.title("Air Quality & Health Risk Prediction")

selected_city = st.selectbox("Select a City", cities)

if st.button("Predict AQI"):
    response = requests.get(
        f"http://127.0.0.1:8000/predict/{selected_city}"
    )
    
    if response.status_code == 200:
        result = response.json()

        st.success(f"City: {result["city"]}")
        st.write("Predicted AQI: ", result["predicted_aqi"])
        st.write("Health Risk: ", result["health_risk"])

    else: 
        st.error("Prediction Failed!!")