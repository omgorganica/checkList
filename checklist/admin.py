from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import VehicleType, VehicleUnit

admin.site.register(VehicleType)
admin.site.register(VehicleUnit)




