from django.shortcuts import render, redirect
from django.http import HttpResponse
import json, requests
from django.views.decorators.csrf import csrf_exempt
import random, string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.forms.models import model_to_dict
# Create your views here.

## Page Display Views

###Display Explore Page
def explore(request):

   return render(request, 'BookFlight/exploreTrip.html')

###Display Departure Flights Page
def displayDepartureFlights(request):

   return render(request, 'BookFlight/displayDepartureFlights.html')

###Display Returning Flights Page
def displayReturningFlights(request):

   return render(request, 'BookFlight/displayReturningFlights.html')

###Display Selected Departing Flight Page
def displaySelectedDepartureFlight(request):

   return render(request, 'BookFlight/displaySelectedDepartingFlight.html')

###Display Selected Returning Flight Page
def displaySelectedReturningFlight(request):

   return render(request, 'BookFlight/displaySelectedReturningFlight.html')

###Display Itenary Page
def displayItenary(request):

   return render(request, 'BookFlight/displayItenary.html')

###Display Passanger Form Page
def displayPassengerPage(request):

   return render(request, 'BookFlight/displayPassengerPage.html')

###Display Flight Review Page
def reviewDetails(request):

   return render(request, 'BookFlight/reviewDetails.html')

###Display Booking Page
def bookingConfirmation(request):

   return render(request, 'BookFlight/bookingConfirmation.html')

###Booking Page
def manageBooking(request):

   return render(request, 'ManageBooking/manageBooking.html')

###Flight Status
def flightStatus(request):

   return render(request, 'FlightStatus/flightStatus.html')

###Display All Member bookings
def allMemberBookings(request):

   return render(request, 'ManageBooking/displayUserBooking.html')

###Display booking By Refernce Number
def bookingByReferenceNumber(request):
 
   return render(request, 'ManageBooking/displayBookingByBrn.html')

###Display status by flight number
def viewStatus(request):
 
   return render(request, 'FlightStatus/viewStatus.html')

def viewStatusByRoute(request):
 
   return render(request, 'FlightStatus/viewStatusByRoute.html')

 

###Display Modify Booking page
def modifyBooking(request):
 
   return render(request, 'ManageBooking/modifyBooking.html')

###Display Modify Departure Flights
def modifyDepartureFlight(request):
 
   return render(request, 'ManageBooking/UpdateDepartureFlight/displayUpdateDepartureFlights.html')

###Display Modify Departure Selected Flights
def modifySelectedDepartureFlight(request):
 
   return render(request, 'ManageBooking/UpdateDepartureFlight/selectedDepartureUpdatedFlight.html')



#----------------------------------------------------------------------------------------------------------------------------#
## Data Processing Views

###Once the Explore Form is submitted
def submitexploreform(request):
  try:
    
    if request.method=="POST":

      tripD = str(request.POST.get('trip'))
      fromD = str(request.POST.get('from')) 
      toD = str(request.POST.get('to')) 
      departD = str(request.POST.get('startdate')) 
      returnD = str(request.POST.get('enddate')) 
      passangerD = str(request.POST.get('passanger'))
      
      #Storing this data in session for further use
      request.session['returnDate']=returnD
      request.session['passanger']=passangerD
      request.session['tripType']=tripD

      data = {

            'tripD':tripD,
            'fromD':fromD,
            'toD':toD,
            'departD':departD,
            'returnD': returnD

      }

      print(data)
      
      #Redirected if trip selected is ONEWAY
      if returnD == "":

       url = "/api/departureFlights/?trip={}&from={}&to={}&departure={}".format(tripD,fromD,toD,departD)
       return redirect(url)   
       
      #Redirected if trip selected is ROUNDTRIP
      else:

       url = "/api/departureFlights/?trip={}&from={}&to={}&departure={}&return={}".format(tripD,fromD,toD,departD,returnD)
       return redirect(url)
      
    return tripD
  
  except:
   pass


#----------------------------------------------------------#
###Once the suitable departing flight is selected
def submitdepartureform(request):
      
     try: 

      if request.method=="GET":
       
       selectedFlightId = request.GET.get("flight_id")
       tripT = request.session['tripType']
       print("Slected flight id is = {}".format(selectedFlightId))
       print("Trip Type is = {}".format(tripT))

       url = "/api/selectedDepartureFlight/?trip={}&flightId={}".format(tripT,selectedFlightId)

       #Storing this data in session for further use
       request.session['dFlightId'] = selectedFlightId

      return redirect(url)
     except:
      pass
 

#----------------------------------------------------------#
###Once the button to display Returning flights is clicked 
def submitreturnform(request):
  
  try:
    if request.method=="POST":

      #Getting To and From value from selected departing flight page(NOT RECOMMENDED)
      #Change to receive it using session variable
      fromD = request.POST.get('fromForm')
      toD = request.POST.get('toForm')


      returnDate = request.session['returnDate']
      
      data = {

            'fromD':fromD,
            'toD':toD,
            'returnDate':returnDate

      }

      url = "/api/returningFlights/?trip={}&from={}&to={}&return={}".format("ROUNDTRIP",fromD,toD,returnDate)

      return redirect(url)
  except:
   pass

#----------------------------------------------------------#
###Once the suitable returning flight is selected
def submitreturnselectedform(request):
      
      
      selectedReturnFlightId = request.GET.get("flight_id")
      print(selectedReturnFlightId)


      url = "/api/selectedReturningFlight/?flightId={}".format(selectedReturnFlightId)

      #Storing this data in session for further use
      request.session['rFlightId'] = selectedReturnFlightId

      return redirect(url)


#----------------------------------------------------------#
###Once the View Trip button is clicked
def submititenaryform(request):
  try:
    
    if request.method=="POST":

      #Retrieving session info
      returningFlight = request.session['rFlightId']
      departingFlight = request.session['dFlightId']
      passanger = request.session['passanger']
      tripType = request.session['tripType']
      

      data = {

            'departingFlight':departingFlight,
            'returningFlight':returningFlight

      }

      if tripType == "ONEWAY":
       url = "/api/itenary/?trip={}&departingFlight={}&passanger={}".format(tripType,departingFlight,passanger)
      
      else: 
       url = "/api/itenary/?trip={}&departingFlight={}&returningFlight={}&passanger={}".format(tripType,departingFlight,returningFlight,passanger)
       
      return redirect(url)
  except:
   pass
  
#----------------------------------------------------------#
###Once the Continue on View Trip Page button is clicked  
def submititenaryPage(request):
  try:
    
    if request.method=="POST":
      
      #Getting data from Itenary page
      tripData = request.POST.get("tripStr")
      tripId = request.POST.get("trip_id")
      print(tripData)
      print(tripId)

      #Storing Itenary data for further use
      request.session['tripInfo'] = tripData
      request.session['trip_id'] = tripId

      #Retrieving Passanger Count
      passanger = request.session['passanger']
      print(passanger)
      

      data = {
            'passanger':passanger,
      }

      url = "/api/passangerPage/?passanger={}".format(passanger)

      return redirect(url)
      
  except:
   pass
  
#----------------------------------------------------------#
###Once the trip data is successfully sent from Itenary page
def redirectPassangerPage(request):
      
   try:  
      passanger = request.session['passanger']
      print(passanger)
      

      data = {
            'passanger':passanger,
      }

      url = "/api/passangerPage/?passanger={}".format(passanger)
      return redirect(url)
   except:
    pass

  
#----------------------------------------------------------#
###Once the submit button is clicked on passanger page
def submitpassangerPage(request):

  if request.method=="POST":

   #Retrieving all info from passanger form
   fName = str(request.POST.get('firstName'))
   lName = str(request.POST.get('lastName')) 
   dob = str(request.POST.get('dob')) 

   # POST Request to create passanger API
   url = "http://localhost:8000/api/passangers/"
   header = {
    "Content-Type":"application/json"
    }
   payload ={
	"firstName": fName,  
	"lastName": lName,
	"dob": dob
   }
   result = requests.post(url,  data=json.dumps(payload), headers=header)
   result_json = result.json()

   #Retrieving passanger ID from response
   passangerId= result_json["id"]
   print(passangerId)

   # Storing passanger ID in session variable
   request.session['passanger_id'] = passangerId
   
   #Retrieving Trip Info TO be sent in URL
   tripD = request.session['tripInfo']

   pData = {

            "fName":fName,
            "lName":lName,
            "dob": dob

      }

   url = "/api/reviewDetails/?passanger={}&trip={}".format(pData, tripD)

   return redirect(url)
  

#----------------------------------------------------------#
###Once the Complete Booking is clicked on Review page
@csrf_exempt
def submitreviewform(request):
  
  try:
    if request.method=="POST":
    
    #---------CARD PROCESSING------------- 
      #Retrieving card data from card form
      cardName = str(request.POST.get('cname'))
      cardNumber = str(request.POST.get('ccnum')) 
      expmonth = str(request.POST.get('expmonth')) 
      expyear = str(request.POST.get('expyear')) 
      cvv = str(request.POST.get('cvv')) 
      
    # POST request to add card to database 
    url = "http://localhost:8000/api/cards/"
    header = {
      "Content-Type":"application/json"
     }
    payload ={
        "nameOnCard": cardName,
        "cardNumber": cardNumber,
        "expiryMonth": expmonth,
        "expiryYear": expyear,
        "cvv": cvv
     }
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    result_json = result.json()
    print(result_json)
    #Retreiving card Id from API response
    cardId= result_json["id"]

    #Storing card ID in session variable
    request.session['card_id'] = cardId

   #-------BOOKING PROCESSING-----
    
    #Is Member
    def checkIsMember():
      if request.user.is_authenticated:
       return True
   
      else:
       return False
      

   
    #Fetch User
    def getUserId1():
      if request.user.is_authenticated:
       return request.user.id
   
      else:
       return 1
    
    #Fetch Trip Id
    trip_Id = request.session['trip_id']
  
    #Fetch Passanger Id
    passanger_Id = request.session['passanger_id']

    #Fetch Card Id
    card_Id = request.session['card_id']

    #Creating Random Booking Refernce Number
    brn= ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    bookingRefernceNumber=brn
    user1 = getUserId1()
    tripId=trip_Id
    passangerId= passanger_Id
    cardId = card_Id
    isMember= checkIsMember()
    contactEmail= "gurkirat2773@gmail.com"

    #POST request to add Booking to database
    url = "http://localhost:8000/api/bookings/"
    header = {
      "Content-Type":"application/json"
     }
    
    print("Prob here1")

    payload ={
        "bookingReferenceNumber": bookingRefernceNumber,
        "user_id": user1,
        "trip_id": tripId,
        "passanger_id": passangerId,
        "payment_id": cardId,
        "isMember": isMember,
        "contactEmail": contactEmail
     }
    
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    result_json = result.json()

    #Retrieving Booking Refernce Number from API response
    bookingId= result_json["bookingReferenceNumber"]

    url = "/api/bookingConfirmation/?bookingReferenceNumber={}".format(bookingId)

    return redirect(url)

  except:
    pass
  
def login_page(request):
  
  if request.method == "POST": 
    usern = request.POST.get('username')
    passw = request.POST.get('password') 

    #usern= '_nav' 
    #passw = '123'

    print(usern, passw)

    if not User.objects.filter(username = usern).exists():
       messages.error(request, 'Invalid Username')
       redirect('/api/loginPage/')

    user = authenticate(username = usern, password = passw )

    if user is None:
       messages.error(request, "Invalid Password")
       redirect('/api/loginPage/')

    else: 
      login(request, user)
      return redirect("/api/exploreTrip/")

      
  
  return render(request,'Authentication/login.html')
  
def register_page(request):
  
  if request.method == "POST":
    firstName = request.POST.get('first_name')
    lastName = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    contact = str(request.POST.get('pn'))
    email = str(request.POST.get('email'))

    user= User.objects.filter(username = username)

    if user.exists():
      messages.info(request, 'Username already exists')
      return redirect('/api/register/')

    user = User.objects.create(
      first_name = firstName,
      last_name = lastName,
      username = username
    )
    user.set_password(password)
  
    user.save()
    
    """

    Need a way to fetch user id of above created user
    print(contact)
    print(email)
    print(user.id)


    #POST request to add Booking to database
    url = "http://localhost:8000/api/membersDetails/"
    
    header = {
      "Content-Type":"application/json"
     }

    payload ={
        "user_id" : 2,
        "contactNumber": contact,
        "emailAddress": email
     }
    
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    result_json = result.json()
  
    print(user)
    print(result_json)

"""

    messages.info(request, 'Account created successfully')
    return redirect('/api/register/')
  return render(request,'Authentication/register.html')

def logout_page(request):
  
  logout(request)

  return redirect("/api/exploreTrip/")

def redirectToAllBookingsPage(request):
  if request.user.is_authenticated:
   
   uid = request.user.id
   print(uid)
   
  
  else:
    uid = "Anonymous"
    
  url = "/api/allBookings/?member={}".format(uid)
  return redirect(url)



@csrf_exempt
def submitManageBookingForm(request):

    if request.method=="POST":
    
    #---------CARD PROCESSING------------- 
      #Retrieving card data from card form
      brn = str(request.POST.get('bookingReferenceNumber'))
      print(brn)

    '''
    # GET Request to Booking API

    api_url = 'http://127.0.0.1:8000/api/bookings/'
    result = requests.get(api_url, params={'bookingReferenceNumber': brn})
    result_json = result.json()

    print(result_json)

  '''
    
    url = "/api/booking/?bookingReferenceNumber={}".format(brn)
    return redirect(url)
   


"""
    #Saving contact details
     user1 = model_to_dict(user)
     print(user)

    #date1= "27-01-11"

    url = "http://localhost:8000/api/membersDetails/"
    header = {
      "Content-Type":"application/json"
     }
    payload ={
    "user" : user1,
    "contactNumber": contact,
    "emailAddress": email
}
    result = requests.post(url,  data=json.dumps(payload), headers=header)
    result_json = result.json()
    print(result_json)



    #-----
"""


def submitflightStatusByFnForm(request):

  if request.method=="POST":

   
   flightNumber = request.POST.get('flightNumber')

   
   #url = "http://localhost:8000/api/realTimeFlightStatus/?flightNumber={}".format(flightNumber)

   #result = requests.get(url)
   #result_json = result.json()
   #print(result_json)


   #flightStatus= result_json["status"]
  # print(flightStatus)


   url = "/api/viewStatus/?flightNumber={}".format(flightNumber)

   return redirect(url)



def submitflightStatusByRouteForm(request):

  if request.method=="POST":

   
   departureAirport = request.POST.get('departureAirport')
   destinationAirport = request.POST.get('destinationAirport')
   departureDate = request.POST.get('departureDate')

   url = "/api/viewStatusByRoute/?departureAirport={}&destinationAirport={}&departureDate={}".format(departureAirport,destinationAirport,departureDate)

   return redirect(url)
  


def submitTripId(request):
      
      
      #Getting data from Itenary page
      trip_id = request.POST.get("tripId")

      request.session['trip_session_id'] = trip_id

      print(trip_id)
      

      data = {
            'trip_id':trip_id,
      }

      url = "/api/modifyBooking/?tripId={}".format(trip_id)
      return redirect(url)


###Once the suitable departing flight is selected
def submitModifydepartureform(request):
      
     try: 

      if request.method=="GET":
       
       selectedFlightId = request.GET.get("flight_id")
       tripT = request.session['tripType']
       print("Slected flight id is = {}".format(selectedFlightId))
       print("Trip Type is = {}".format(tripT))

       url = "/api/modifySelectedDepartureFlight/?trip={}&flightId={}".format(tripT,selectedFlightId)

       #Storing this data in session for further use
       request.session['dFlightId'] = selectedFlightId

      return redirect(url)
     except:
      pass

