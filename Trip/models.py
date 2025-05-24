from django.db import models
from Flight.models import Flight,Airport
from django.contrib.auth.models import User
import string
import random
#from AirArctic.Member.models import Member
# Create your models here.



class Trip(models.Model):

    TRIP_CHOICE = (
    ("ROUNDTRIP" , "Round Trip"),
    ("ONEWAY" , "One way"),
     )

    trip = models.CharField(max_length=15,choices=TRIP_CHOICE, default="ROUNDTRIP")
   # tripDescription = Flight.departureAirport + "TO" + Flight.destinationAirport
    #departingFlight = models.ForeignKey(Flight, on_delete=models.PROTECT, default=1, related_name = 'departingFlight')
    departingFlight = models.ForeignKey(Flight, on_delete=models.PROTECT, default=1, related_name = 'departingFlight')
    returningFlight = models.ForeignKey(Flight, on_delete=models.PROTECT, default=1, related_name = 'returningFlight')


class Passengers(models.Model):

    
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dob = models.DateField()


       
    def __str__(self)-> str:
        return self.firstName
    

class CardDetails(models.Model):

    
    nameOnCard = models.CharField(max_length=100)
    cardNumber = models.CharField(max_length=16)
    expiryMonth = models.CharField(max_length=2)
    expiryYear = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)


       
    def __str__(self)-> str:
        return self.nameOnCard
    

# using random.choices() generating random strings



class Booking(models.Model):
 
     bookingReferenceNumber = models.CharField(max_length=10)
     user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
     trip = models.ForeignKey(Trip, on_delete=models.PROTECT, default=1)
     passanger = models.ForeignKey(Passengers, on_delete=models.PROTECT, default=1)
     payment = models.ForeignKey(CardDetails, on_delete=models.PROTECT, default=1)
     isMember = models.BooleanField(default = False)
     contactEmail = models.EmailField()



    


