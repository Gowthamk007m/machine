from django.urls import path,include
from .views import AddAirport,SearchLongest,SearchSortest
urlpatterns = [
    path('',AddAirport.as_view(),name='add_airport'),
    path('search/',SearchLongest.as_view(),name='search'),
    path('search-sortest/',SearchSortest.as_view(),name='search_sortest'),

]