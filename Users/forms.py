from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
