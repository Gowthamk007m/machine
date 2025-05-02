from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView,CreateView
from .forms import AirportroutesForm,AirportCreationForm, SearchForm
from .models import Airportroutes,Connetion
# Create your views here.


class Home(View):
    def get(self, request):
        return render(request,'home.html')
class AddAirport(CreateView):
    template_name='add_airport.html'
    form_class = AirportCreationForm
    success_url='/'

    def get(self, request):
        return render(request,self.template_name)
    
class AddAirportRoutes(CreateView):
    template_name='add_routes.html'
    form_class = AirportroutesForm
    success_url='/add_routes'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SearchRoutesLongest(View):
    def get(self, request):
        form=SearchForm()
        return render(request,'search.html',{'form':form})
    
    def post(self, request):
        form=SearchForm(request.POST)
        # try:
        if form.is_valid():
            takeoff_code=request.POST['takeoff_code']
            destination_code=request.POST['destination_code']
        
            connections = Connetion.objects.filter(takeoff_code=takeoff_code,destination_code=destination_code).order_by('-duration')
            data=connections[0]
            return render(request,'search.html',{'data':data})
        # except:
        #     return HttpResponse("No Routes Found")



class SearchRoutesSortest(View):
    def get(self, request):
        form=SearchForm()
        return render(request,'search.html',{'form':form})
    
    def post(self, request):
        form=SearchForm(request.POST)
        # try:
        if form.is_valid():
            takeoff_code=request.POST['takeoff_code']
            destination_code=request.POST['destination_code']
            connections = Connetion.objects.filter(takeoff_code=takeoff_code,destination_code=destination_code).order_by('duration')
            data=connections[0]
            return render(request,'search.html',{'data':data})
        # except:
        #     return HttpResponse("No Routes Found"
