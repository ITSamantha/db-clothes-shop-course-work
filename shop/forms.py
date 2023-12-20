from django import forms

from shop.models import Demand
from users.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'name': 'user_name', 'placeholder': 'Your Name',
                                           'class': 'form-control border-0 py-4'}),
            'email': forms.EmailInput(attrs={'name': 'user_email', 'placeholder': 'Your Email',
                                             'class': 'form-control border-0 py-4'}),
        }


class DemandForm(forms.ModelForm):
    name = forms.CharField(max_length=64,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.CharField(max_length=128,
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    subject = forms.CharField(max_length=64,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message',
                                     'data-validation-required-message': 'Please enter message.'}))

    class Meta:
        model = Demand
        fields = ('name', 'email', 'subject', 'message')
