# forms.py
from django import forms
from .models import AirportRoute, Airport

class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = AirportRoute
        fields = ['from_airport', 'to_airport', 'position', 'duration']

class SearchNthNodeForm(forms.Form):
    start_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
    direction = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')])
    n = forms.IntegerField(min_value=1)
