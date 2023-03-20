import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data

# Add title, text input, slider, select box, sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider(
    "Forecast Days",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days"
)

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky Conditions"))
st.subheader(f"Temperature for the next {days} days in {place}")

# Get the temperature/ sky conditions

if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            # Create a temperature plot
            temperatures = [t['main']['temp'] / 10 for t in filtered_data]
            dates = [d["dt_txt"] for d in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        if option == "Sky Conditions":
            images = {
                "Clear": "images/clear.png", "Clouds": "images/cloud.png",
                "Rain": "images/rain.png", "Snow": "images/snow.png"
            }
            sky_conditions = [t['weather'][0]['main'] for t in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("Sorry I don't recognize that location")
