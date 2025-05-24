from django.contrib import admin
from .models import Trip, Booking, CardDetails, Passengers

# Register your models here.

admin.site.register(Trip)
admin.site.register(Booking)
admin.site.register(CardDetails)
admin.site.register(Passengers)


