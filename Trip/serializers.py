from rest_framework import serializers
from .models import Trip, Passengers, CardDetails, Booking
from Flight.serializers import FlightSerializer
from Member.serializers import CurrentUserSerializer
from Flight.models import Flight, Airport
from django.contrib.auth.models import User

class TripSerializer1(serializers.ModelSerializer):

    departingFlight = FlightSerializer(read_only = True)
    returningFlight = FlightSerializer(read_only = True)

    departingFlight_id = serializers.IntegerField(write_only = True)
    returningFlight_id = serializers.IntegerField(write_only = True)


    class Meta:
        model = Trip

        fields = ['id','departingFlight', 'departingFlight_id','returningFlight', 'returningFlight_id']

    #def get_trip_description(self, obj, departureAirport, destinationAirport):
     #    return departureAirport.iataCode + "TO" + destinationAirport.iataCode
        
     
            
class TripSerializer2(serializers.ModelSerializer):

    departingFlight = FlightSerializer(read_only = True)
    #returningFlight = FlightSerializer(read_only = True)

    departingFlight_id = serializers.IntegerField(write_only = True)
    #returningFlight_id = serializers.IntegerField(write_only = True)


    class Meta:
        model = Trip

        fields = ['id','departingFlight', 'departingFlight_id']



class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ['id', 'firstName', 'lastName', 'dob']

class CardDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDetails
        fields = ['id', 'nameOnCard', 'cardNumber', 'expiryMonth', 'expiryYear', 'cvv']

"""
class BookingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Booking
        fields = ['bookingReferenceNumber','user', 'trip', 'passanger', 'payment','isMember', 'contactEmail']
"""
class BookingSerializer(serializers.ModelSerializer):

    passanger = PassangerSerializer(read_only = True)
    payment = CardDetailsSerializer(read_only = True)
    trip = TripSerializer1(read_only = True)
    user = CurrentUserSerializer(read_only = True)

    passanger_id = serializers.IntegerField(write_only = True)
    payment_id = serializers.IntegerField(write_only = True)
    trip_id = serializers.IntegerField(write_only = True)
    user_id = serializers.IntegerField(write_only = True)
    

    class Meta:
        model = Booking
        fields = ['id','bookingReferenceNumber','user', 'trip', 'passanger', 'payment','isMember', 'contactEmail','passanger_id', 'payment_id', 'trip_id', 'user_id' ]