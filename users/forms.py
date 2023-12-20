from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.validators import RegexValidator

from users.models import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'height:50px;'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'height:50px;'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=64, label='Username*',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'style': 'height:50px;'}))
    first_name = forms.CharField(max_length=128, label='First Name*',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'style': 'height:50px;'}))
    last_name = forms.CharField(max_length=128, label='Last Name*',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'style': 'height:50px;'}))
    email = forms.CharField(max_length=150, label='Email*',
                            widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'style': 'height:50px;'}))

    password1 = forms.CharField(label='Password*', max_length=150,
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'style': 'height:50px;'}))

    password2 = forms.CharField(label='Confirm Password*', max_length=150,
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'style': 'height:50px;'}))

    sex = forms.CharField(label='Sex*', widget=forms.Select(choices=User.Sex.choices,
                                                            attrs={'class': 'form-control',
                                                                   'style': 'height:50px;'}))

    birthday = forms.DateField(label='Birth Date',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date',
                                                             'style': 'height:50px;'}), required=False)

    mobile_phone = forms.CharField(max_length=12, label='Mobile Phone',
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'style': 'height:50px;'}), required=False)

    image = forms.ImageField(label='User Photo', widget=forms.ClearableFileInput(attrs={'class': 'form-control',
                                                                                        'style': 'height:50px;'}),
                             required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',
                  'sex', 'birthday', 'mobile_phone', 'image')


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(label='User Photo', widget=forms.FileInput(attrs={'class': 'form-control',
                                                                               'style': 'height:50px;'}),
                             required=False)

    username = forms.CharField(max_length=64, label='Username',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'style': 'height:50px;', 'readonly': True}))
    first_name = forms.CharField(max_length=128, label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'style': 'height:50px;'}))
    last_name = forms.CharField(max_length=128, label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'style': 'height:50px;'}))
    email = forms.CharField(max_length=150, label='Email',
                            widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'style': 'height:50px;'}))
    sex = forms.CharField(label='Sex', widget=forms.Select(choices=User.Sex.choices,
                                                           attrs={'class': 'form-control',
                                                                  'style': 'height:50px;'}))

    birthday = forms.DateField(label='Birth Date',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date',
                                                             'style': 'height:50px;'}), required=False)

    mobile_phone = forms.CharField(max_length=12, label='Mobile Phone',
                                   widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'style': 'height:50px;'}), required=False)

    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'username',
                  'email', 'sex', 'birthday', 'mobile_phone')


class ReviewForm(forms.ModelForm):
    description = forms.CharField(
        label='Your Review *',
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'cols': 30}),
        max_length=500,
    )
    rating = forms.DecimalField(
        label='Your Rating',
        min_value=0,
        max_value=5,
        decimal_places=1,
        initial=5,
        widget=forms.NumberInput(attrs={'step': 0.5, 'class': 'form-control'}),
    )

    class Meta:
        model = Review
        fields = ('rating', 'description')
