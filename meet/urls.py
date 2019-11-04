from django.urls import path
from . import views

urlpatterns = [
    path('options',views.option),
    path('chat/<slug:slug>',views.messagerieuser),
    path('listechats',views.choicemsg),
    path('detail/<slug:slug>',views.detailuser),
]