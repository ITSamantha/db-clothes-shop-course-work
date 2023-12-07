from django import forms


class SubscribeForm(forms.Form):
    name = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'name': 'user_name', 'required': 'required', 'placeholder': 'Your Name',
               'class': 'form-control border-0 py-4'}))
    email = forms.CharField(max_length=128, widget=forms.TextInput(
        attrs={'name': 'user_email', 'required': 'required', 'placeholder': 'Your Email',
               'class': 'form-control border-0 py-4'}))
