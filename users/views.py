from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm, ProfileForm
from shop.forms import SubscribeForm


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user and user.is_active:  # Block
                login(request, user)
                print(request.user)
                return redirect('index')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def logout_user(request):
    logout(request)
    return render(request, 'products/index.html')


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context=context)


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully subscribed :)')
    else:
        form = SubscribeForm()
    context = {
        'form': form,
    }
    return render(request, 'shop/includes/subscribe.html', context=context)


class Http403(Exception):
    pass


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = ProfileForm(instance=request.user)
        else:
            form = ProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'The new data has been successfully saved!')
                return redirect('users:profile')
        context = {
            'form': form,
        }
        return render(request, 'users/profile.html', context=context)
    else:
        raise Http403("Access forbidden.")
