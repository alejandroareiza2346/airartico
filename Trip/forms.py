from django import forms
from .models import Passengers, CardDetails, Booking

class PassangersForm(forms.ModelForm):
    class Meta:
        model = Passengers
        fields = '__all__'

class CardDetailsForm(forms.ModelForm):
    class Meta:
        model = CardDetails
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

