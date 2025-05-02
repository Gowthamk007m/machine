from django import forms
from .models import Airportroutes,Connetion

class AirportroutesForm(forms.ModelForm):
    class Meta:
        model = Connetion
        fields = ['node','current_code','position','duration']
        
