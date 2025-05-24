
    async function getFlights(from, to) {



        let flights =await  fetch(`http://127.0.0.1:8000/api/flights/?departureAirport=${from}&destinationAirport=${to}`);

        flights = await flights.json()
        console.warn(flights)
        document.getElementById('flightData').innerHTML=flights.map((flight) => 
            `<tr>
                <td>${flight.id}</td>
                <td>${flight.flightNumber}</td>
                <td>${flight.departureAirport.iataCode}</td>
                <td>${flight.destinationAirport.iataCode}</td>
                <td>${flight.departureDate}</td>
                <td>${flight.departureTime}</td>
                <td>${flight.arrivalDate}</td>
                <td>${flight.arrivalTime}</td>
                <td><input type="button"  value="Select Flight" onClick="makeTrip(selectedDepartingFlight=${flight.id})"> </td>
            </tr>`
        
        ).join("");
    }


    async function getReturningFlights(from, to) {



        let flights =await  fetch(`http://127.0.0.1:8000/api/flights/?departureAirport=${to}&destinationAirport=${from}`);
    
        flights = await flights.json()
        console.warn(flights)
        document.getElementById('returningFlightData').innerHTML=flights.map((flight) => 
            `<tr>
                <td>${flight.id}</td>
                <td>${flight.flightNumber}</td>
                <td>${flight.departureAirport.iataCode}</td>
                <td>${flight.destinationAirport.iataCode}</td>
                <td>${flight.departureDate}</td>
                <td>${flight.departureTime}</td>
                <td>${flight.arrivalDate}</td>
                <td>${flight.arrivalTime}</td>
                <td><input type="button"  value="Select Flight" onClick="makeTrip(selectedDepartingFlight=${flight.id})"> </td>
            </tr>`
        
        ).join("");
    }

    async function makeTrip(selectedDepartingFlight) { 

        
            
        const rawResponse = await fetch(`http://127.0.0.1:8000/api/trips/?trip=${trip}`, {
          method: 'POST',
          body: JSON.stringify({
            "departingFlight_id": selectedDepartingFlight,
            "returningFlight_id":2,
    
          }),
          headers: {
            'Content-type': 'application/json; charset=UTF-8',
         },
      });
      const content = await rawResponse.json();
    
      console.log(content);
      document.getElementById('tripData').innerHTML=JSON.stringify(content)
    
        }