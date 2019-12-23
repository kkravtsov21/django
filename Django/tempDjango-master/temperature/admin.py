from django.contrib import admin
from .models import Sensor
from .models import Temperature

admin.site.register(Sensor)
admin.site.register(Temperature)
# Register your models here.
