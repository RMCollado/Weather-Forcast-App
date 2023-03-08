import os
import requests

API_KEY = os.environ.get("OWM_API_KEY")


def get_data(place, forecast_days=None, weather_type=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if weather_type == "Temperature":
        filtered_data = [t['main']['temp'] for t in filtered_data]
    if weather_type == "Sky Conditions":
        filtered_data = [t['weather'][0]['main'] for t in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, weather_type="Temperature"))

