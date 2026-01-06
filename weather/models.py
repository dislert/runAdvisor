from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class WeatherSnapshot(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='weather_snapshots'
    )
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    humidity = models.IntegerField()
    precipitation = models.FloatField()
    date_checked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.city.name} — {self.date_checked.strftime("%Y-%m-%d %H:%M")}'


class RunRecommendation(models.Model):
    weather = models.OneToOneField(
        WeatherSnapshot,
        on_delete=models.CASCADE,
        related_name='run_recommendation'
    )
    comfort_score = models.IntegerField()
    is_good_for_run = models.BooleanField()
    explanation = models.TextField()

    def __str__(self):
        return f'Recommendation for {self.weather.city.name}'
