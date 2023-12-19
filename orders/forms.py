from django import forms

from orders.models import Order, PaymentType
from shop.models import CountryCity


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, label='First Name*',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    last_name = forms.CharField(max_length=128, label='Last Name*',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Surname'}))
    email = forms.CharField(max_length=128, label='Email*',
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    mobile_phone = forms.CharField(max_length=12, label='Mobile Phone*',
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'Your Mobile Phone'}))
    country_city = forms.ModelChoiceField(label='Country, City*',
                                          queryset=CountryCity.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}),
                                          empty_label='Not selected'
                                          )
    address = forms.CharField(label='Address*', max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Address'}))
    postal_code = forms.CharField(label='Postal Code*', max_length=6, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Postal Code'}))
    payment_type = forms.ModelChoiceField(label='Payment Type*',
                                          queryset=PaymentType.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}),
                                          empty_label='Not selected'
                                          )

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'mobile_phone',
                  'country_city', 'address', 'postal_code', 'payment_type']
