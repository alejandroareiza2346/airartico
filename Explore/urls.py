
from django.urls import path, include
from . import views


urlpatterns = [


    #Page Display Endpoints
    
    path('exploreTrip/',views.explore),
    path('departureFlights/',views.displayDepartureFlights, name='displayDepartureFlights'),
    path('returningFlights/',views.displayReturningFlights, name='displayReturningFlights'),
    path('selectedDepartureFlight/',views.displaySelectedDepartureFlight, name='displaySelectedDepartureFlight'),
    path('selectedReturningFlight/',views.displaySelectedReturningFlight, name='displaySelectedReturningFlight'),
    path('itenary/',views.displayItenary, name='displayItenary'),
    path('passangerPage/',views.displayPassengerPage, name='displayPassengerPage'),
    path('reviewDetails/',views.reviewDetails, name='reviewDetails'),
    path('bookingConfirmation/',views.bookingConfirmation, name='bookingConfirmation'),
    path('loginPage/',views.login_page, name='login_page'),
    path('register/',views.register_page, name='register_page'),
    path('logout/',views.logout_page, name='logout_page'),
    path('allBookings/',views.allMemberBookings, name='allMemberBookings'),
    path('booking/',views.bookingByReferenceNumber, name='bookingByReferenceNumber'),
     path('manageBooking/',views.manageBooking, name='manageBooking'),
    path('flightStatus/',views.flightStatus, name='flightStatus'),
    path('viewStatus/',views.viewStatus, name='viewStatus'),
    path('viewStatusByRoute/',views.viewStatusByRoute, name='viewStatusByRoute'),
    path('modifyBooking/',views.modifyBooking, name='modifyBooking'),
    path('modifyDepartureFlight/',views.modifyDepartureFlight, name='modifyDepartureFlight'),
    path('modifySelectedDepartureFlight/',views.modifySelectedDepartureFlight, name='modifySelectedDepartureFlight'),
    
    

    
    #Processing/Redirecting Endpoints


    path('submitForm/',views.submitexploreform, name='submitexploreform'),
    path('submitdepartureForm/',views.submitdepartureform, name='submitdepartureform'),
    path('submitreturnForm/',views.submitreturnform, name='submitreturnform'),
    path('submitreturnselectedForm/',views.submitreturnselectedform, name='submitreturnselectedform'), 
    path('submititenaryform/',views.submititenaryform, name='submititenaryform'),
    path('submititenaryPage/',views.submititenaryPage, name='submititenaryPage'),
    path('redirectPassangerPage/',views.redirectPassangerPage, name='redirectPassangerPage'),
    path('submitpassangerPage/',views.submitpassangerPage, name='submitpassangerPage'),
    path('submitreviewform/',views.submitreviewform, name='submitreviewform'),
    path('redirectToAllBookings/',views.redirectToAllBookingsPage, name='redirectToAllBookingsPage'),
    path('submitManageBookingForm/',views.submitManageBookingForm, name='submitManageBookingForm'),
    path('submitflightStatusByFnForm/',views.submitflightStatusByFnForm, name='submitflightStatusByFnForm'),
    path('submitflightStatusByRouteForm/',views.submitflightStatusByRouteForm, name='submitflightStatusByRouteForm'),
    path('submitTripId/',views.submitTripId, name='submitTripId'),
    path('submitModifydepartureform/',views.submitModifydepartureform, name='submitModifydepartureform'),
    
]