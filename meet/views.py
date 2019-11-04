from django.shortcuts import render
from .forms import SettingsForm,chat
from users.models import utilisateur
from .models import message
from django.http import HttpResponseRedirect,HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from users.models import utilisateur as user

@login_required
def option(request):
    if request.user.is_authenticated:
        listutils=[]
        util=request.user
        form=SettingsForm(initial={'categorie' : util.categorie})
        if request.method=='POST':
            form=SettingsForm(request.POST)
            if form.is_valid():
                util.categorie=form.cleaned_data["categorie"]
                util.save()
                if request.user.categorie==None:
                    listutils=utilisateur.objects.filter(pk!=util.pk)  
                else:
                    listutils=utilisateur.objects.filter(categorie=request.user.categorie) & utilisateur.objects.exclude(pk=util.pk) 
        return render(request,'meet/option.html',{"form":form,"liste":listutils})
    else:
        return HttpResponseRedirect("/")

@login_required
def choicemsg(request):
    T=[]
    listmsg=message.objects.filter(utilto=request.user) | message.objects.filter(utilfrom=request.user)
    for x in listmsg:
        if x.utilto!=request.user:
            T.append(x.utilto)
        else:
            T.append(x.utilfrom)
    return render(request,'meet/choicemsg.html',{"liste":set(T)})

@login_required
def detailuser(request,slug):
    try:
        user1=utilisateur.objects.get(pk=slug)
    except:
        return HttpResponseNotFound("not found")
    return render(request,'meet/details.html',{"utilisateur":user1})

@login_required
def messagerieuser(request,slug):
    try:
        user1=utilisateur.objects.get(pk=slug)
    except:
        return HttpResponseNotFound("not found")
    listmessages=message.objects.filter(utilfrom=request.user,utilto=user1) | message.objects.filter(utilfrom=user1,utilto=request.user)
    form=chat()
    if request.method == 'POST':
        form=chat(request.POST)
        if form.is_valid():
            newmessage=message(utilfrom=request.user,utilto=user1,texte=form.cleaned_data["texte"])
            newmessage.save()
    return render(request,'meet/chat.html',{"liste":listmessages,"form":form})
