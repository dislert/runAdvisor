from django.contrib import admin
from .models import City, WeatherSnapshot, RunRecommendation


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "latitude", "longitude")
    search_fields = ("name",)


@admin.register(WeatherSnapshot)
class WeatherSnapshotAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "temperature",
        "wind_speed",
        "humidity",
        "precipitation",
        "date_checked",
    )
    list_filter = ("city", "date_checked")
    search_fields = ("city__name",)


@admin.register(RunRecommendation)
class RunRecommendationAdmin(admin.ModelAdmin):
    list_display = (
        "weather",
        "comfort_score",
        "is_good_for_run",
    )
    list_filter = ("is_good_for_run",)
    search_fields = ("weather__city__name",)
