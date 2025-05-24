from django.shortcuts import render
from django.db import models
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip, Passengers, CardDetails, Booking
from Flight.models import Flight
from .serializers import TripSerializer1, TripSerializer2, PassangerSerializer, CardDetailsSerializer, BookingSerializer
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PassangersForm, CardDetailsForm, BookingForm
from rest_framework import generics

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
def retrieveAllTrips(request):

    if request.method == 'GET':
        trips = Trip.objects.all()
        serialized_item = TripSerializer1(trips, many=True)

        return Response(serialized_item.data)

    if request.method == 'POST':
       
       '''
       
       #Departing & returning Flight Id sent in the URL by client app
       #http://127.0.0.1:8000/api/trips/?trip=roundtrip&departingFlightId ={flight.FlightId}&returningFlightId ={flight.FlightId}
       trip_type = request.query_params.get('trip')
       departing_flight_id = request.query_params.get('departingFlightId')
       returning_flight_id = request.query_params.get('returningFlightId')

       #Condition to check if roundtrip has both returningFlightId & departing flight Id

       #if trip_type =="Roundtrip":
         
       if departing_flight_id and returning_flight_id:

            flights = Flight.objects.all()
            

            #Condition to fetch flight objects using ID's

            departingFlightObj = flights.filter(id = departing_flight_id)
            returningFlightObj = flights.filter(id = returning_flight_id)

            Trip.trip = trip_type
            Trip.departingFlight = departingFlightObj
            Trip.returningFlight = returningFlightObj

            trip = Trip.save()

            
            serialized_item = TripSerializer(trip)
            #serialized_item.is_valid(raise_exception=True)
            #serialized_item.save()
    return Response(serialized_item.data, status.HTTP_201_CREATED)

    
           ''' 
       
    trip = request.query_params.get('trip')


    if trip == 'ROUNDTRIP':

     print("Roundtrip serializer used")
           
     serialized_item = TripSerializer1(data = request.data)

     serialized_item.is_valid(raise_exception=True)

     serialized_item.save()
            
     return Response(serialized_item.data, status.HTTP_201_CREATED )

    elif trip == 'ONEWAY':
      
      print("Oneway serializer used")
      Trip.departingFlight_id == None   
       
      serialized_item = TripSerializer2(data = request.data)

      serialized_item.is_valid(raise_exception=True)

      serialized_item.save()
            
      return Response(serialized_item.data, status.HTTP_201_CREATED )
    
#Retrieve specific Trip by  Trip Id
@api_view(['GET'])
def retrieveSingleTrip(request,id):
    if request.method == 'GET':
        trip  = Trip.objects.get(pk=id)
        serialized_item = TripSerializer1(trip)
        return Response(serialized_item.data)
    
class TripUpdateView(generics.UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer1
    
    

#Retrieve All the  Passangers

@api_view(['GET','POST'])
def retrieveAllPassanger(request):

    if request.method == 'GET':
        passanger = Passengers.objects.all()
        serialized_item = PassangerSerializer(passanger, many=True)
        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = PassangerSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)
    

#Retrieve specific Pasanger by  Passanger Id
@api_view(['GET','POST'])
def retrieveSinglePassanger(request,id):
    if request.method == 'GET':
        passanger  = Passengers.objects.get(pk=id)
        serialized_item = PassangerSerializer(passanger)
        return Response(serialized_item.data)
    

def viewPassanger(request):
    
   if request.method == 'GET':
    
    items = Passengers.objects.all()

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
   return render(request, "passangerView.html", itemData)

def addPassanger(request):
   form = PassangersForm()
   if request.method == 'POST':
      form = PassangersForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form': form}
   return render(request, 'passangerForm.html', context)


# Card Details


#Retrieve All the  Passangers

@api_view(['GET','POST'])
def retrieveAllCards(request):

    if request.method == 'GET':
        cards = CardDetails.objects.all()
        serialized_item = CardDetailsSerializer(cards, many=True)
        return Response(serialized_item.data)

    if request.method == 'POST':
       serialized_item = CardDetailsSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)
    

#Retrieve specific card by  Card Id
@api_view(['GET','POST'])
def retrieveSingleCard(request,id):
    if request.method == 'GET':
        card  = CardDetails.objects.get(pk=id)
        serialized_item = CardDetailsSerializer(card)
        return Response(serialized_item.data)
    

def viewCards(request):
    
   if request.method == 'GET':
    
    items = CardDetails.objects.all()

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
   return render(request, "cardView.html", itemData)

def addCard(request):
   form = CardDetailsForm()
   if request.method == 'POST':
      form = CardDetailsForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form': form}
   return render(request, 'cardForm.html', context)


# Booking Details


#Retrieve All the  Bookings

@api_view(['GET','POST'])
def retrieveAllBookings(request):

    if request.method == 'GET':
        
        booking_obj = Booking.objects.all()

        booking_reference_number = request.query_params.get('bookingReferenceNumber')
        member = request.query_params.get('member')
      
        #Filter results based on departure airport sent in the URL by client App
        if booking_reference_number:
           booking_obj = booking_obj.filter(bookingReferenceNumber = booking_reference_number)

        #Filter results based on departure airport sent in the URL by client App
        if member:
           booking_obj = booking_obj.filter(user = member)

        serialized_item = BookingSerializer(booking_obj, many=True)
        return Response(serialized_item.data)
    


    if request.method == 'POST':
       serialized_item = BookingSerializer(data = request.data)
       serialized_item.is_valid(raise_exception=True)
       serialized_item.save()
       return Response(serialized_item.data, status.HTTP_201_CREATED)
    
       
    

#Retrieve specific booking by  Booking Id
@api_view(['GET','POST'])
def retrieveSingleBooking(request,id):
    if request.method == 'GET':
        booking  =Booking.objects.get(pk=id)
        serialized_item = BookingSerializer(booking)
        return Response(serialized_item.data)

class BookingUpdateView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

#Delete specific booking by  Booking Id
@api_view(['DELETE'])
def deleteBooking(request,id):   
    if request.method == 'DELETE':
        booking  =Booking.objects.get(pk=id)
        booking.delete()
        return Response("Booking Deleted")
       
    

def viewBookings(request):
    
   if request.method == 'GET':
    
    items = Booking.objects.all()

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
   return render(request, "bookingView.html", itemData)

def addBooking(request):
   form = BookingForm()
   if request.method == 'POST':
      form = BookingForm(request.POST)
      if form.is_valid():
         form.save()

   context = {'form': form}
   return render(request, 'bookingForm.html', context)


