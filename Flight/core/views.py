from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView,CreateView
from .forms import AirportroutesForm
from .models import Airportroutes,Connetion
# Create your views here.

class AddAirport(CreateView):
    template_name='add_routes.html'
    form_class = AirportroutesForm
    success_url='/'

    def form_valid(self, form):
        new_code=Airportroutes(code=self.request.POST['current_code'])
        new_code.save()

        form.save()
        return super().form_valid(form)


class SearchLongest(View):
    template_name='search.html'
    def get(self, request):
        connections = Connetion.objects.all().order_by('-duration')
        data=connections[0]
        return render(request,self.template_name,{'data':data})
    
class SearchSortest(View):
    template_name='search.html'
    
    def get(self, request):
        connections = Connetion.objects.all().order_by('duration')
        data=connections[0]
        return render(request,self.template_name,{'data':data})