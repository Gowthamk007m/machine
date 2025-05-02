from django import forms
from .models import Airportroutes,Connetion


class AirportCreationForm(forms.ModelForm):
    class Meta:
        model = Airportroutes
        fields = ['code']

class AirportroutesForm(forms.ModelForm):
    class Meta:
        model = Connetion
        fields = ['takeoff_code','destination_code','position','duration']
        
class FindNthNode(forms.ModelForm):
    class Meta:
        model=Connetion
        fields=['destination_code']
        


class SearchForm(forms.ModelForm):
    class Meta:
        model = Connetion
        takeoff_code = forms.ModelChoiceField(queryset=Airportroutes.objects.all())
        destination_code = forms.ModelChoiceField(queryset=Airportroutes.objects.all())
        fields = ['takeoff_code','destination_code']

