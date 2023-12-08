from django import forms

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
