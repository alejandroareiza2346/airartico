from django.db import models

# Create your models here.

class Airport(models.Model):

    iataCode = models.CharField(max_length=3)
    airportName = models.CharField(max_length=100)
    airportLocation = models.CharField(max_length=100)

    def __str__(self)-> str:
        return self.airportName

class Aircraft(models.Model):
    
    aircraftModel = models.CharField(max_length=100)

    def __str__(self)-> str:
        return self.aircraftModel
''' 
class Financial(models.Model):

    airTransportationCharge = models.DecimalField(decimal_places=2)
    airportImprovementFee = models.DecimalField(decimal_places=2)
    airTravellerSecurityCharge = models.DecimalField(decimal_places=2)
    goodsAndServiceCharge = models.DecimalField(decimal_places=2)
'''
class Flight(models.Model):

    flightNumber = models.CharField(max_length=100)
    airCraft = models.ForeignKey(Aircraft, on_delete=models.PROTECT, default=1, related_name = 'departureAirport')
    departureAirport = models.ForeignKey(Airport, on_delete=models.PROTECT, default=1, related_name = 'destinationAirport')
    destinationAirport = models.ForeignKey(Airport, on_delete=models.PROTECT, default=1)
    departureDate = models.DateField()
    arrivalDate = models.DateField()
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()
    seatsAvailableToBook = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5, default= 250)

    def __str__(self)-> str:
        return self.flightNumber
    
FLIGHT_STATUS_CHOICES = (
    ("Scheduled ", "Scheduled "),
    ("Delayed ", "Delayed "),
    ("Departed", "Departed"),
    ("In Air", "In Air"),
    ("Landed", "Landed"),
    ("Arrived", "Arrived"),
    ("Cancelled", "Cancelled "),
    ("Expected", "Expected"),
    ("Past Flight", "Past Flight"),
    ("Diverted", "Diverted"),
)

class FlightStatus(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT, default=1)
    status = models.CharField(max_length=15, choices= FLIGHT_STATUS_CHOICES, default = "Scheduled")
    
    
    def __str__(self)-> str:
        return self.flight
