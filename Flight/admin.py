from django.contrib import admin
from .models import Flight, Aircraft, Airport, FlightStatus

# Register your models here.

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(FlightStatus)