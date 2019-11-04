from django.shortcuts import render
from .forms import InscriptionForm,LoginForm
from .models import utilisateur
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def inscription(request):
    if not request.user.is_authenticated:
        form=InscriptionForm()
        if request.method=='POST':
            form=InscriptionForm(request.POST)
            if form.is_valid():
                user=utilisateur.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],password=form.cleaned_data['password'])
                login(request,user)
                return HttpResponseRedirect('/')
        return render(request,'users/inscription.html',{"form":form})
    else:
        return HttpResponseRedirect("/app/options")

def loginview(request):
    if not request.user.is_authenticated:
        form=LoginForm()
        if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/app/options')
        return render(request,'users/welcome.html',{"form":form})
    else:
        return HttpResponseRedirect("/app/options")

def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')