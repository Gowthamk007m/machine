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
 
    main_results=[]
    results = []
    parent_name=''
    count=0
    if form.is_valid():
            query = form.cleaned_data['search_query']
            data = NewAiportModel.objects.filter(name__icontains=query)
            checkView(request,data)
            
            # left_check=AirportConnections.objects.filter(child_left__in=data).values('parent__name','child_left__name')
            # right_check=AirportConnections.objects.filter(child_right__in=data).values('parent__name','child_right__name')
            
            # if left_check:
            #     # results.append(left_check)
            #     parent_name=left_check[0]['parent__name']
            #     print(parent_name)
            #     if parent_name:
            #         results.append(parent_name)
            #         print("yes")
            #     else:
            #         print("no")
                    
            #         count=1
                
                
            
            # if right_check:
            #     # results.append(right_check)
            #     parent_name=right_check[0]['parent__name']
            #     print(parent_name)
                
            #     if parent_name:
            #         results.append(parent_name)
            #         print("yes")
                    
            #     else:
            #         print("no")
                    
            #         count=1
                    
            
            
            
            
        # results=AirportConnections.objects.filter(child_left__in=data)
    return render(request, 'search.html', {'form': form, 'results': results})

def checkView(request,data):
    results = []
    parent_name=data[0]
    name_of_data=data[0]
    in_data=data
    the_head="A"
    new_parent_name=name_of_data
    
    current_node=""
    
    while new_parent_name!=the_head:
        
        # data = NewAiportModel.objects.filter(name__icontains=query)
        # print("Inital Current node",new_parent_name)
        left_check=AirportConnections.objects.filter(child_left__name=new_parent_name).values('parent__name','child_left__name','duration_left')
        right_check=AirportConnections.objects.filter(child_right__name=new_parent_name).values('parent__name','child_right__name','duration_right')
        
        # print("left check",left_check)
        # print("right check",right_check)
        
        if left_check:
            # results.append(left_check)
            new_parent_name=left_check[0]['parent__name']
            
            if new_parent_name!=the_head:
                
                results.append({new_parent_name})
                results.append(left_check[0]['duration_left'])
                
                current_node=new_parent_name
                # print("Current node",current_node)
                
            else:
                results.append(the_head)
                results.append(left_check[0]['duration_left'])
                
                # print("reached A")
                                
        if right_check:
            
            # # results.append(right_check)
            new_parent_name=right_check[0]['parent__name']
            
            if parent_name!=the_head:
                results.append(new_parent_name)
                results.append(right_check[0]['duration_right'])
                current_node=new_parent_name
                # print("current_node",current_node)

            else:
                results.append(the_head)
                results.append(right_check[0]['duration_right'])
                
                # print("reached A")
          
        
        

        
                    
            
            
            
        
        print(results)