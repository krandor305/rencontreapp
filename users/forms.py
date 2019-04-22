from . import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class InscriptionForm(ModelForm):
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
        username=forms.CharField(max_length=100)
        password = forms.CharField(widget=forms.PasswordInput())