from django import forms
from .models import Sensor, Temperature

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = "__all__"

class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = "__all__"