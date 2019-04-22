from django.shortcuts import render
from .forms import InscriptionForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def inscription(request):
    form=InscriptionForm()
    if request.method=='POST':
        form=InscriptionForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],password=form.cleaned_data['password'])
            login(request,user)
            return HttpResponseRedirect('/')
    return render(request,'users/inscription.html',{"form":form})

def loginview(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
    return render(request,'users/inscription.html',{"form":form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')