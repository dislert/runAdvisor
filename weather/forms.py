from django import forms
from django.core.validators import RegexValidator

class WeatherInputForm(forms.Form):
    city_name = forms.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z\s\-]+$',
                message='Город должен быть написан только на английском (латиница)',
                code='invalid_city'
            )
        ]
    )

