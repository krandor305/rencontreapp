from . import models
from users.models import utilisateur
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SettingsForm(forms.Form):
    categorie = forms.CharField(max_length=100)

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'

class chat(forms.Form):
    texte=forms.CharField(max_length=300,label='')

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'
