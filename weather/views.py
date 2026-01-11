from django.shortcuts import render
from .models import City, WeatherSnapshot, RunRecommendation
from .services import calculate_run_comfort
from .forms import WeatherInputForm


def index(request):
    recommendation = None

    if request.method == "POST":
        form = WeatherInputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            city, _ = City.objects.get_or_create(
                name=data.get("city_name", "Пользовательский город"),
                latitude=0,
                longitude=0
            )

            # Создание записи погоды
            weather = WeatherSnapshot.objects.create(
                city=city,
                temperature=data["temperature"],
                wind_speed=data["wind_speed"],
                humidity=data["humidity"],
                precipitation=data["precipitation"]
            )

            result = calculate_run_comfort(weather)

            # Создание рекомендации
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
            "recommendation": recommendation
        }
    )
