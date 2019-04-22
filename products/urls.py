
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('select/<slug:slug>',views.detail),
    path('products/add',views.addproduit),
    path('products/mycreations',views.productsUser),
    path('products/delete/<slug:slug>',views.deleteproduit),
]
