from django import forms
from .models import Airport, Aircraft, Flight, FlightStatus

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'

class AircraftForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        fields = '__all__'

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightStatusForm(forms.ModelForm):
    class Meta:
        model = FlightStatus
        fields = '__all__'