from rest_framework import serializers
from .models import Airport, Aircraft, Flight, FlightStatus

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['id', 'iataCode', 'airportName', 'airportLocation']

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'aircraftModel']

class FlightSerializer(serializers.HyperlinkedModelSerializer):


    departureAirport = AirportSerializer(read_only=True)
    destinationAirport = AirportSerializer(read_only=True)
    airCraft = AircraftSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = ['id', 'flightNumber', 'airCraft', 'departureAirport', 'destinationAirport', 'departureDate', 'arrivalDate', 'departureTime', 'arrivalTime', 'seatsAvailableToBook','price' ]


    def calculateFlightTime():
        flightTime =  Flight.departureTime - Flight.arrivalTime
        return flightTime
        
class FlightStatusSerializer(serializers.HyperlinkedModelSerializer):


    flight = FlightSerializer(read_only=True)

    flight_id = serializers.IntegerField(write_only = True)


    class Meta:
        model = FlightStatus
        fields = ['id', 'flight', 'flight_id', 'status']

