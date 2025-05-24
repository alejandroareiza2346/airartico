
   
async function makeTrip(selectedDepartingFlight, selectedReturningFlight, trip) { 

        
            
    const rawResponse = await fetch(`http://127.0.0.1:8000/api/trips/?trip=${trip}`, {
      method: 'POST',
      body: JSON.stringify({
        "departingFlight_id": selectedDepartingFlight,
        "returningFlight_id": selectedReturningFlight,

      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
     },
  });
  const content = await rawResponse.json();

  console.log(content);
  return content;
  

    }


  async function addPassanger(firstName,lastName,dob) { 

        
            
      const rawResponse = await fetch(`http://localhost:8000/api/passangers/`, {
        method: 'POST',
        body: JSON.stringify({
          "firstName": firstName,
          "lastName": lastName,
          "dob": dob,
  
        }),
        headers: {
          'Content-type': 'application/json; charset=UTF-8',
       },
    });
      const passanger = await rawResponse.json();
  
      console.log(passanger);
      return passanger;
    
  
      }


   
   
async function getFlights(from, to, departure) {
      

        let flights =await fetch(`http://127.0.0.1:8000/api/flights/?departureAirport=${from}&destinationAirport=${to}&departureDate=${departure}`);

        flights = await flights.json()
        console.warn(flights)
        return flights


        console.log("Orignal func")

}

async function getFlightById(flightId) {




  let flight =await  fetch(`http://127.0.0.1:8000/api/flight/${flightId}`);

  flight = await flight.json()
  console.warn(flight)
  return flight


  console.log("GetFlight by If func")

}


function storesTripData(from, to){

  console.log(from)
  console.log(to)

}




async function getReturningFlights(from, to, returnDate) {



        let flights =await  fetch(`http://127.0.0.1:8000/api/flights/?departureAirport=${to}&destinationAirport=${from}&departureDate=${returnDate}`);
    
        flights = await flights.json()
        console.warn(flights)
        return flights
        
    }


async function getStatus(flightNumber) {
      

      let flightStatus =await fetch(`http://localhost:8000/api/realTimeFlightStatus/?flightNumber==${flightNumber}`);

      flightStatus = await flightStatus.json()
      console.warn(flightStatus)
      return flightStatus


      console.log("Orignal func")

}


  



    function storeDepartingFlightId(selectedDepartingFlightId){
      console.log(selectedDepartingFlightId);
      return selectedDepartingFlightId;
      
    }

    function takeToReturningFlightPage(){
      return window.location.href = "{% url 'displayDepartureFlights' %}"
    
    }

    
async function getBookingByReferenceNumber(bookingReferenceNumber) {
      

      let booking =await fetch(`http://127.0.0.1:8000/api/bookings/?bookingReferenceNumber=${bookingReferenceNumber}`);

      booking = await booking.json()
      console.warn(booking)
      return booking

}

async function deleteBookingById(bookingId) {
      

  let booking =await fetch(`http://127.0.0.1:8000/api/bookings/?bookingReferenceNumber=${bookingReferenceNumber}`);

  booking = await booking.json()
  console.warn(booking)
  return booking

}

