from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import FireTeam  # Import the Team model instead of FireTeam

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )

class TeamForm(forms.ModelForm):
    class Meta:
        model = FireTeam  # Reference the Team model
        fields = ['name', 'members']
