from django.contrib import admin
from .models import flight, airport, passenger
# Register your models here.
class flightadmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class passengeradmin(admin.ModelAdmin):
    filter_horizontal = ("allflights",)

admin.site.register(airport)
admin.site.register(flight, flightadmin)
admin.site.register(passenger, passengeradmin)