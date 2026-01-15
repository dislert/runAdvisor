from django.shortcuts import render
from .models import City, WeatherSnapshot, RunRecommendation
from .services import calculate_run_comfort
from .forms import WeatherInputForm
from .api import fetch_weather_by_city


def index(request):
    recommendation = None
    error = None

    if request.method == "POST":
        form = WeatherInputForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data["city_name"]

            weather_data = fetch_weather_by_city(city_name)

            if not weather_data:
                error = "Город не найден"
            else:
                city, _ = City.objects.get_or_create(
                    name=city_name,
                    latitude=weather_data["latitude"],
                    longitude=weather_data["longitude"]
                )

                weather = WeatherSnapshot.objects.create(
                    city=city,
                    temperature=weather_data["temperature"],
                    wind_speed=weather_data["wind_speed"],
                    humidity=weather_data["humidity"],
                    precipitation=weather_data["precipitation"]
                )

                result = calculate_run_comfort(weather)

                recommendation = RunRecommendation.objects.create(
                    weather=weather,
                    comfort_score=result["comfort_score"],
                    is_good_for_run=result["is_good_for_run"],
                    explanation=result["explanation"]
                )
    else:
        form = WeatherInputForm()

    return render(
        request,
        "weather/analyze.html",
        {
            "form": form,
            "recommendation": recommendation,
            "error": error
        }
    )
