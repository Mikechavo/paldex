from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm, TeamForm
from .models import FireTeam
from paldex.models import PalModel 

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

def add_to_fire_team(request, pal_name, fire_team_id):
    fire_team = get_object_or_404(FireTeam, pk=fire_team_id)
    if fire_team:
        fire_team.members[pal_name] = True  # Add the member to the dictionary
        fire_team.save()  # Save the updated fire team
        return redirect('fire_team_detail', fire_team_id=fire_team.id)
    else:
        # Handle the case where the fire team does not exist
        messages.error(request, "No Fire Team found")
        return redirect('home')  # Redirect to the home page or an appropriate page



def delete_fire_team(request, fire_team_id):
    fire_team = get_object_or_404(FireTeam, pk=fire_team_id)
    if request.method == 'POST':
        fire_team.delete()
        return redirect('home')  # Redirect to the home page or any other appropriate URL
    return render(request, 'confirm_delete_fire_team.html', {'fire_team': fire_team})


def remove_pal_from_fire_team(request, pal_name, fire_team_id):
    fire_team = get_object_or_404(FireTeam, pk=fire_team_id)
    if fire_team:
        if pal_name in fire_team.members:
            del fire_team.members[pal_name]  # Remove the pal from the dictionary
            fire_team.save()  # Save the updated fire team
            return redirect('fire_team_detail', fire_team_id=fire_team.id)
        else:
            # Handle the case where the pal does not exist in the fire team
            messages.error(request, "Pal not found in Fire Team")
    else:
        # Handle the case where the fire team does not exist
        messages.error(request, "No Fire Team found")
    return redirect('home')  # Redirect to the home page or an appropriate page



