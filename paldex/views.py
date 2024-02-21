# views.py
from django.shortcuts import render
from .models import PalModel

def home_view(request):
    return render(request, 'home.html')

def pals_view(request):
    pal_data = PalModel.objects.all()
    return render(request, 'pals.html', {'pal_data': pal_data})

def contact_view(request):
    return render(request, 'contact.html')

def search_view(request):
    query = request.GET.get('q')
    pal_data = None
    
    if query:
        # Search for pals whose type matches the query
        pal_data = PalModel.objects.filter(type__icontains=query.lower())
        
        # If no results found, check if any pal has the query as one of its types
        if not pal_data:
            pal_data = PalModel.objects.filter(type__icontains=query.lower())
    
    return render(request, 'search_results.html', {'query': query, 'pal_data': pal_data})

