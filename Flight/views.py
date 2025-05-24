from django.shortcuts import render
from django.db import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Aircraft, Airport, Flight, FlightStatus
from .serializers import FlightSerializer, AircraftSerializer, AirportSerializer, FlightStatusSerializer
from django.core.paginator import Paginator, EmptyPage
from .forms import AirportForm, AircraftForm, FlightForm, FlightStatusForm
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.decorators import permission_classes

# Create your views here.

#========
# API Implementation 
#========

#Retrieve All the real time flights

@api_view(['GET','POST'])
def retrieveAllFlights(request):

    if request.method == 'GET':
        flights = Flight.objects.all()

        departure_airport = request.query_params.get('departureAirport')
        destination_airport = request.query_params.get('destinationAirport')
        departure_date = request.query_params.get('departureDate')
    

        #Filter results based on departure airport sent in the URL by client App
        if departure_airport:
           flights = flights.filter(departureAirport__iataCode = departure_airport)

        #Filter results based on destination airport sent in the URL by client App
        if destination_airport:
           flights = flights.filter(destinationAirport__iataCode = destination_airport)

        #Filter results based on departure date sent in the URL by client App
        if departure_date:
           flights = flights.filter(departureDate = departure_date)

        #Filter results based on seatsAvailableToBook sent in the URL by client App

        serialized_item = FlightSerializer(flights, many=True)


        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = FlightSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)
    

#Retrieve specific flight by Id
@api_view(['GET','POST'])
def retrieveSingleFlight(request,id):
    if request.method == 'GET':
        flight = Flight.objects.get(pk=id)
        serialized_item = FlightSerializer(flight)

        return Response(serialized_item.data)

# ----------------------------------------------------------

#Retrieve All the real time flight status

@api_view(['GET','POST'])
def retrieveAllFlightStatus(request):

    if request.method == 'GET':
        flightStatus = FlightStatus.objects.all()
        flights = Flight.objects.all()

        departure_airport = request.query_params.get('departureAirport')
        destination_airport = request.query_params.get('destinationAirport')
        departure_date = request.query_params.get('departureDate')
        flight_number = request.query_params.get('flightNumber')
    

        #Filter results based on departure airport sent in the URL by client App
        if departure_airport:
           flights = flights.filter(departureAirport__iataCode = departure_airport)
           flightStatus = flightStatus.filter(flight__in = flights)

        #Filter results based on destination airport sent in the URL by client App
        if destination_airport:
           flights = flights.filter(destinationAirport__iataCode = destination_airport)
           flightStatus = flightStatus.filter(flight__in = flights)

       #Filter results based on flight Number sent in the URL by client App
        if flight_number:
           flights = flights.filter(flightNumber = flight_number)
           flightStatus = flightStatus.filter(flight__in = flights)

        #Filter results based on departure date sent in the URL by client App
        if departure_date:
           flights = flights.filter(departureDate = departure_date)
           flightStatus = flightStatus.filter(flight__in = flights)

        #Filter results based on seatsAvailableToBook sent in the URL by client App

        serialized_item = FlightStatusSerializer(flightStatus, many=True)


        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = FlightStatusSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)
    

#Retrieve specific flight status by Id
@api_view(['GET','POST'])
def retrieveSingleFlightStatus(request,id):
    if request.method == 'GET':
        flightStatus = FlightStatus.objects.get(pk=id)
        serialized_item = FlightStatusSerializer(flightStatus)

        return Response(serialized_item.data)

# ----------------------------------------------------------

#Retrieve All the  Airports

@api_view(['GET','POST'])
def retrieveAllAirports(request):

    if request.method == 'GET':
        airports = Airport.objects.all()
        serialized_item = AirportSerializer(airports, many=True)
        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = AirportSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)
    

#Retrieve specific airport by  Airport Id
@api_view(['GET','POST'])
def retrieveSingleAirport(request,id):
    if request.method == 'GET':
        airport  = Airport.objects.get(pk=id)
        serialized_item = AirportSerializer(airport)
        return Response(serialized_item.data)
    
    # ----------------------------------------------------------------------

    
#Retrieve All the  Aircrats

@api_view(['GET','POST'])
def retrieveAllAircrats(request):

    if request.method == 'GET':
        aircrats = Aircraft.objects.all()
        serialized_item = AircraftSerializer(aircrats, many=True)
        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = AircraftSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)
    

#Retrieve specific airport by  Airport Id
@api_view(['GET','POST'])
def retrieveSingleAircraft(request,id):
    if request.method == 'GET':
        aircraft  = Aircraft.objects.get(pk=id)
        serialized_item = AircraftSerializer(aircraft)
        return Response(serialized_item.data)
    

    #------------------------------------------------------



#========
# WebApp Implementation 
#========


def airportView(request):
    
   if request.method == 'GET':
    
    items = Airport.objects.all()

    perpage = request.GET.get('perpage', default=2)
    page = request.GET.get('page', default = 1)
    paginator = Paginator(items, per_page=perpage)

    try:
       items = paginator.page(number=page)

    except EmptyPage:
       items = []

    totalPages = items.paginator.num_pages

    itemData = {
       
       'items': items,
       'lastpage': totalPages,
       'totalPageList': [n+1 for n in range(totalPages)],

    }
   return render(request, "flightForm.html", itemData)

def addAirport(request):
   form = AirportForm()
   if request.method == 'POST':
      form = AirportForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form': form}
   return render(request, 'airportForm.html', context)



def aircraftView(request):
    
   if request.method == 'GET':

    items = Aircraft.objects.all()

    perpage = request.GET.get('perpage', default=2)
    page = request.GET.get('page', default = 1)
    paginator = Paginator(items, per_page=perpage)

    try:
       items = paginator.page(number=page)

    except EmptyPage:
       items = []
   
    totalPages = items.paginator.num_pages

    itemData = {      
       'items': items,
       'lastpage': totalPages,
       'totalPageList': [n+1 for n in range(totalPages)],
    }
   return render(request, "aircraftView.html", itemData)



def addAircraft(request):
   form = AircraftForm()
   if request.method == 'POST':
      form = AircraftForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form': form}
   return render(request, 'aircraftForm.html', context)


def addFlight(request):
   form = FlightForm()
   if request.method == 'POST':
      form = FlightForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form': form}
   return render(request, 'flightInfoForm.html', context)


#Index

def index(request):

   return render(request, 'index.html')

   #========
# WebApp Implementation 
#========


def flightView(request):
    
   if request.method == 'GET':

    flights = Flight.objects.all()


    #paginator = Paginator(items, 2)
    
    #perpage = request.query_params.get('perpage', default=2)
    #page = request.query_params.get('page', default = 1)

    perpage = request.GET.get('perpage', default=15)
    page = request.GET.get('page', default = 1)

    paginator = Paginator(flights, per_page=perpage)

    

    try:
       flights = paginator.page(number=page)

    except EmptyPage:
       flights = []

   
    totalPages = flights.paginator.num_pages


    flightsData = {
       
       'flights': flights,
       'lastpage': totalPages,
       'totalPageList': [n+1 for n in range(totalPages)],

    }
   return render(request, "flightsDisplay.html", flightsData)

#----------------------------------

def flightStatusView(request):
    
   if request.method == 'GET':
    
    items = FlightStatus.objects.all()

    perpage = request.GET.get('perpage', default=10)
    page = request.GET.get('page', default = 1)
    paginator = Paginator(items, per_page=perpage)

    try:
       items = paginator.page(number=page)

    except EmptyPage:
       items = []

    totalPages = items.paginator.num_pages

    itemData = {
       
       'items': items,
       'lastpage': totalPages,
       'totalPageList': [n+1 for n in range(totalPages)],

    }
   return render(request, "flightStatusDisplay.html", itemData)

def addFlightStatus(request):
   form = FlightStatusForm()
   if request.method == 'POST':
      form = FlightStatusForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form': form}
   return render(request, 'FlightStatusForm.html', context)