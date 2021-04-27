from django.contrib import admin

from .models import EarthHumidity, AirInformation

admin.site.register(EarthHumidity)
admin.site.register(AirInformation)