from django import forms


class WeatherInputForm(forms.Form):
    city_name = forms.CharField(
        label="Город",
        max_length=100
    )
