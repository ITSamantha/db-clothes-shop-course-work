from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

import users.forms
from shop.forms import SubscribeForm
from users.models import Subscribe


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = users.forms.LoginForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:  # Block
                login(request, user)
                return redirect('index')
    else:
        form = users.forms.LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def logout_user(request):
    logout(request)
    return render(request, 'users/login.html')


def register_user(request):
    return render(request, 'users/register.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user_name = cleaned_data['name']
            user_email = cleaned_data['email']
            sub = Subscribe(name=user_name, email=user_email)
            sub.save()
            messages.success(request, 'Form submission successful')
    else:
        form = SubscribeForm()
    context = {
        'form': form,
    }
    return render(request, 'shop/includes/subscribe.html', context=context)
