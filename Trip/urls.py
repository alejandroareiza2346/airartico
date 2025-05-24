
from django.urls import path, include
from . import views
from .views import TripUpdateView, BookingUpdateView



urlpatterns = [

    path('trips/',views.retrieveAllTrips),
    path('trip/<int:id>',views.retrieveSingleTrip),

    path('tripUpdate/<int:pk>/', TripUpdateView.as_view(), name='trip-update'),


    # Fetch Passangers endpoints
    path('passangers/',views.retrieveAllPassanger),
    path('passanger/<int:id>',views.retrieveSinglePassanger),

    path('passangerForm/',views.addPassanger, name='passangerForm'),
    path('passangerView/',views.viewPassanger, name='passangerView'),

        # Card Details endpoints
    path('cards/',views.retrieveAllCards),
    path('card/<int:id>',views.retrieveSingleCard),

    path('cardForm/',views.addCard, name='cardForm'),
    path('cardView/',views.viewCards, name='cardView'),

    
        # Booking endpoints
    path('bookings/',views.retrieveAllBookings),
    path('booking/<int:id>',views.retrieveSingleBooking),
    path('deleteBooking/<int:id>', views.deleteBooking, name='deleteBooking'),

    path('bookingForm/',views.addBooking, name='bookingForm'),
    path('bookingView/',views.viewBookings, name='bookingView'),
    path('bookingUpdate/<int:pk>/', BookingUpdateView.as_view(), name='booking-update'),

]