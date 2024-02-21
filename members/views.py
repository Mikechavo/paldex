from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm, TeamForm
from .models import FireTeam
from paldex.views import get_pals_data
from django.db.models import QuerySet

# from paldex.models import PalModel 

import logging

logger = logging.getLogger(__name__)

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
            # Set the leader_id field to the current user's ID
            fire_team = form.save(commit=False)
            fire_team.leader_id = request.user.id
            fire_team.save()
            # Redirect to the home page or any other appropriate URL after creating the team
            return redirect('home')
    else:
        form = TeamForm()
    return render(request, 'create_team.html', {'form': form})

def fire_team_detail(request, fire_team_id):
    fire_team = FireTeam.objects.get(pk=fire_team_id)
    return render(request, 'authenticate/fire_team_detail.html', {'fire_team': fire_team})

def add_to_fire_team(request, pal_Name, fire_team_id):
    # Call the get_pals_data function to retrieve the data
    pals_data = get_pals_data()
    
    # Iterate over the pals_data to find the desired pal
    pal = next((pal for pal in pals_data if pal['Name'] == pal_Name), None)
    fire_team = get_object_or_404(FireTeam, pk=fire_team_id)

    logger.info(f"Pal Name: {pal_Name}, Pal: {pal}, Fire Team: {fire_team}")

    if fire_team is not None:
        if len(fire_team.members) >= 5:
            messages.error(request, "Fire Team is full, please remove one or more Pals")
        else:
            # Ensure that fire_team.members is a queryset
            if isinstance(fire_team.members, QuerySet):
                # Add the pal to the fire team members
                fire_team.members.add(pal)
                # Redirect to the Fire Team detail page after adding the Pal
                return redirect('fire_team_detail', fire_team_id=fire_team.id)
            else:
                messages.error(request, "Fire Team members is not a valid queryset")
    else:
        messages.error(request, "No Fire Team found")
    # Redirect to an appropriate page or handle the error as needed
    return redirect('home')  # Redirect to the home page for example





def delete_fire_team(request, fire_team_id):
    fire_team = get_object_or_404(FireTeam, pk=fire_team_id)
    if request.method == 'POST':
        fire_team.delete()
        return redirect('home')  # Redirect to the home page or any other appropriate URL
    return render(request, 'confirm_delete_fire_team.html', {'fire_team': fire_team})

def remove_pal_from_fire_team(request, fire_team_id, pal_Name):
    fire_team = get_object_or_404(FireTeam, pk=fire_team_id)
    pal = next((pal for pal in pals_data if pal['Name'] == pal_Name), None)
    if request.method == 'POST':
        fire_team.members.remove(pal)
        return redirect('fire_team_detail', fire_team_id=fire_team_id)  # Redirect to the fire team detail page
    return render(request, 'confirm_remove_pal.html', {'fire_team': fire_team, 'pal': pal})


