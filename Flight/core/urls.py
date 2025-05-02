from django.urls import path,include
from .views import AddAirport,AddAirportRoutes,SearchRoutesLongest,SearchRoutesSortest,Home
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add_airport/',AddAirport.as_view(),name='add_airport'),
    path('add_routes/',AddAirportRoutes.as_view(),name='add_routes'),
    path('search-longest/',SearchRoutesLongest.as_view(),name='search_longest'),
    path('search-sortest/',SearchRoutesSortest.as_view(),name='search_sortest'),
]