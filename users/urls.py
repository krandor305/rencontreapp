from django.urls import path
from . import views

urlpatterns = [
    path('inscription',views.inscription),
    path('',views.loginview),
    path('logout',views.logoutview),
]