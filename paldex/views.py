# views.py
from django.shortcuts import render
from .models import PalModel


def home_view(request):
    return render(request, 'home.html')

def pals_view(request):
    pal_data = PalModel.objects.all()
    return render(request, 'pals.html', {'pal_data': pal_data})
