from . import models
from .models import utilisateur
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class InscriptionForm(ModelForm):
    class Meta:
        model = utilisateur
        fields=['username','email','first_name','last_name','password']
        widgets = {
            'password': forms.PasswordInput(),
        }
    
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'