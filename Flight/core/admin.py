from django.contrib import admin
from .models import Airport,AirportRoute
from django.contrib.admin import site
# Register your models here.

site.register(Airport)
site.register(AirportRoute)
