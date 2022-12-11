from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newsclip", views.newsclip, name="newsclip"),
    path("allauth", views.allauth, name="allauth"),
    path("investor", views.investor, name="investor"),
    path("deal", views.deal, name="deal"),
    path("company", views.company, name="company"),
]
