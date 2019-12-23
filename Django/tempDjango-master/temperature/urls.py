from django.contrib import admin
from django.urls import path
from temperature import views

urlpatterns += [
    path('catalog/', include('admin.site.urls')),
]
