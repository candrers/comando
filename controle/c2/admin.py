from dataclasses import fields
from django.contrib import admin
from typing import Union

# Register your models here.
from .models import Dispositivo

@admin.register(Dispositivo)

class DispositivoAdmin(admin.ModelAdmin):
   fields=['title', 'latitude', 'longitude', 'icon', 'ip', 'mac', 'pub_date']
    