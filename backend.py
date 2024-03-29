import os
import requests
import streamlit as st

# Windows API
# API_KEY = os.environ.get("OWM_API_KEY")

# Streamlit API Key
API_KEY = st.secrets["OWM_API_KEY"]


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=imperial"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    pass


