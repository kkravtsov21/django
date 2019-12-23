"""tempDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from temperature import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temperature_module/', views.index),
    path('temperature_module/locations/', views.locations),
    path('temperature_module/temperatures/', views.temperatures),
    path('temperature_module/sensor_form/', views.sensorForm),
    path('temperature_module/temperature_form/', views.temperatureForm),
    path('temperature_module/exports/', views.exports),
    path('temperature_module/exports/xml/', views.export_xml),
    path('temperature_module/exports/docx/', views.export_docx),
]
