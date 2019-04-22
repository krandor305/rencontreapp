from . import models
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class addproductForm(ModelForm):
    class Meta:
        model = models.Productsinnovation
        fields=['nom','Description','Image']

class addmessageForm(ModelForm):
    class Meta:
        model = models.message
        fields=['nom']
        labels = {
            "nom": "commentaire"
        }
