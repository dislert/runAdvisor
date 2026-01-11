from django import forms


class WeatherInputForm(forms.Form):
    temperature = forms.FloatField(
        label="Температура (°C)",
        min_value=-10,
        max_value=40
    )
    wind_speed = forms.FloatField(
        label="Скорость ветра (м/с)",
        min_value=0,
        max_value=50
    )
    humidity = forms.IntegerField(
        label="Влажность (%)",
        min_value=0,
        max_value=100
    )
    precipitation = forms.FloatField(
        label="Осадки (мм)",
        min_value=0,
        max_value=100
    )
