# views.py
from django.shortcuts import render
from .models import PalModel

def home_view(request):
    pal_data = PalModel.objects.all()
    return render(request, 'home.html', {'pal_data': pal_data})
