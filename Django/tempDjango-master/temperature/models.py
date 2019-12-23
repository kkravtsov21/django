from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Temperature(models.Model):
    date = models.DateField(auto_now = True)
    time = models.TimeField(auto_now = True)
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + " " + str(self.time)
# Create your models here.
