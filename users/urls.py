from django.urls import path
from . import views

urlpatterns = [
    path('inscription',views.inscription),
    path('login',views.loginview),
    path('logout',views.logoutview),
]