from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from .forms import SearchForm
from .models import *

def home_page(request): # Example view to display the search form
    form = SearchForm()
    return render(request, 'home.html', {'form': form})

def search_results(request):
    form=SearchForm(request.GET)
    results = []
    max_results=0
    min_results=0
    if form.is_valid():
            query = form.cleaned_data['search_query']
            data = NewAiportModel.objects.filter(name__icontains=query)
            results=checkView(request,data)
            print(results)
            max_results=max(results)
            print(max_results)
            min_results=min(results)

            
    return render(request, 'search.html', {'form': form, 'results': results,'max_results':max_results,'min_results':min_results})

def checkView(request,data):
    results = []
    name_of_data=data[0].name
    the_head="A"
    new_parent_name=name_of_data
    final=[]
    
    if new_parent_name==the_head:
        return results

    results.append(name_of_data)
    
    while new_parent_name!=the_head:
        unchanged_parent=new_parent_name
        left_check=AirportConnections.objects.filter(child_left__name=new_parent_name).values('parent__name','child_left__name','duration_left')
        right_check=AirportConnections.objects.filter(child_right__name=new_parent_name).values('parent__name','child_right__name','duration_right')
        
        if left_check:
            new_parent_name=left_check[0]['parent__name']
            
            if new_parent_name!=the_head:
                results.append(unchanged_parent)
                
                results.append(left_check[0]['duration_left'])
                results.append(new_parent_name)
            else:
                results.append(unchanged_parent)
                results.append(left_check[0]['duration_left'])
                results.append(the_head)
                                
        if right_check:
            new_parent_name=right_check[0]['parent__name']
            
            if new_parent_name!=the_head:
                results.append(unchanged_parent)
                
                results.append(right_check[0]['duration_right'])
                results.append(new_parent_name)
            else:
                results.append(unchanged_parent)
                results.append(right_check[0]['duration_right'])
                results.append(the_head)
                
        
        results.reverse()
        final.append(results)
        results=[]
    final.reverse()
    

    return final