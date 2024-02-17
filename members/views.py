from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm, TeamForm
from .models import FireTeam
from paldex.models import PalModel 

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pals')
        else:
            messages.error(request, "There was an error logging in, please try again")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration complete!")
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form': form})

def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', team_id=team.id)
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})

def team_detail(request, team_id):
    team = FireTeam.objects.get(pk=team_id)
    return render(request, 'team_detail.html', {'team': team})

def add_to_fire_team(request, pal_name):
    pal = get_object_or_404(PalModel, name=pal_name)
    fire_team = FireTeam.objects.first()

    if fire_team is not None:
        if fire_team.members.count() >= 5:
            messages.error(request, "Fire Team is full, please remove one or more Pals")
        else:
            fire_team.members.add(pal)
            return redirect('fire_team_detail')  # Redirect to the correct URL
    else:
        # Handle the case where no FireTeam exists
        messages.error(request, "No Fire Team found")
        # Redirect to an appropriate page or handle the error as needed
        return redirect('home')  # Redirect to the home page for example

