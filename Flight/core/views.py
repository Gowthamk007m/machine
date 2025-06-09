from django.shortcuts import render
from .models import *
from .forms import *


def get_nth_node(start_airport, direction, n):
    current = start_airport
    for _ in range(n):
        try:
            route = AirportRoute.objects.get(from_airport=current, position=direction)
            current = route.to_airport
        except AirportRoute.DoesNotExist:
            return None  # No more nodes in that direction
    return current

def get_longest_route():
    return AirportRoute.objects.order_by('-duration').first()

def find_shortest_path(start, end, visited=None, current_duration=0):
    if visited is None:
        visited = set()

    if start == end:
        return current_duration

    visited.add(start)

    shortest = float('inf')
    for route in AirportRoute.objects.filter(from_airport=start):
        if route.to_airport not in visited:
            duration = find_shortest_path(route.to_airport, end, visited.copy(), current_duration + route.duration)
            if duration is not None:
                shortest = min(shortest, duration)

    return shortest if shortest != float('inf') else None



def add_route_view(request):
    form = AirportRouteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'add_route.html', {'form': form})

def search_nth_node_view(request):
    result = None
    if request.method == 'POST':
        form = SearchNthNodeForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_airport']
            direction = form.cleaned_data['direction']
            n = form.cleaned_data['n']
            result = get_nth_node(start, direction, n)
    else:
        form = SearchNthNodeForm()
    return render(request, 'search.html', {'form': form, 'result': result})