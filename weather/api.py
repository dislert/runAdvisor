import requests


def fetch_weather_by_city(city_name):
    # 1. Получаем координаты города
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_response = requests.get(
        geo_url,
        params={"name": city_name, "count": 1},
        timeout=10
    )
    geo_response.raise_for_status()
    geo_data = geo_response.json()

    if not geo_data.get("results"):
        raise ValueError("Город не найден")

    city_info = geo_data["results"][0]

    latitude = city_info["latitude"]
    longitude = city_info["longitude"]

    # 2. Получаем погоду
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_response = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "wind_speed_10m",
                "precipitation",
            ],
        },
        timeout=10
    )
    weather_response.raise_for_status()
    weather_data = weather_response.json()["current"]

    return {
        "temperature": weather_data["temperature_2m"],
        "humidity": weather_data["relative_humidity_2m"],
        "wind_speed": weather_data["wind_speed_10m"],
        "precipitation": weather_data["precipitation"],
        "latitude": latitude,
        "longitude": longitude,
    }
