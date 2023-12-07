from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Login', 'style': 'height:50px;'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'height:50px;'}))


class RegistrationForm():
    pass
