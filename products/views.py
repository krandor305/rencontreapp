from django.shortcuts import render
from .models import Products,Productsinnovation,message
from django.http import HttpResponseNotFound,HttpResponseRedirect
from .forms import addproductForm,addmessageForm

def index(request):
    products=Productsinnovation.objects.all()
    return render(request,'products/index.html',{"products":products})


def productsUser(request):
    products=Productsinnovation.objects.filter(innovateur=request.user)
    return render(request,'products/tableau.html',{"products":products})

def deleteproduit(request,slug):
    try:
        produit=Productsinnovation.objects.get(pk=slug,innovateur=request.user)
        if request.user.is_authenticated:
            produit.delete()
            return HttpResponseRedirect("/products/mycreations")
        else:
            return HttpResponseNotFound('<h1>Page not found</h1>')
    except Productsinnovation.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')

def addproduit(request):
    if request.user.is_authenticated:
        form=addproductForm()
        if request.method=='POST':
            form=addproductForm(request.POST)
            if form.is_valid():
                form.instance.innovateur=request.user
                form.save()
                return HttpResponseRedirect('/products/mycreations')
        return render(request,'products/form.html',{"form":form})
    else:
        return HttpResponseNotFound('<h1>connectez vous</h1>')

def addmessage(request,slug):
    if request.user.is_authenticated:
        form=addmessageForm()
        if request.method=='POST':
            form=addmessageForm(request.POST)
            if form.is_valid():
                form.instance.innovateur=request.user
                form.instance.Produit=Productsinnovation.objects.get(pk=slug)
                form.save()
        return HttpResponseRedirect('/select/'+slug)
    else:
        return HttpResponseNotFound('<h1>connectez vous</h1>')

def detail(request,slug):
    try:
        product=Productsinnovation.objects.get(pk=slug)
        messages=message.objects.filter(Produit=product)
        if request.user.is_authenticated:
            form2=addmessageForm()
            if request.method=='POST':
                form2=addmessageForm(request.POST)
                if form2.is_valid():
                    form2.instance.innovateur=request.user
                    form2.instance.Produit=Productsinnovation.objects.get(pk=slug)
                    form2.save()
                    return HttpResponseRedirect('/select/'+slug)
        else:
            return HttpResponseNotFound('<h1>connectez vous</h1>')
        if product.innovateur==request.user:
            form=addproductForm(instance=product)
            if request.method=='POST':
                form=addproductForm(request.POST,instance=product)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/products/mycreations')
            return render(request,'products/form.html',{"form":form,"form2":form2,"messages":messages})
        return render(request,'products/detail.html',{"form":form2,"product":product})
    except Products.DoesNotExist:
        return HttpResponseNotFound("<h1>not found</h1>")
    
