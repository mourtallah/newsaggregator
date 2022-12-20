from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newsclip", views.newsclip, name="newsclip"),
    path("allauth", views.allauth, name="allauth"),
    path("investor", views.investor, name="investor"),
    path("deal", views.deal, name="deal"),
    path("company", views.company, name="company"),
    path("new_deal", views.new_deal, name="new_deal"),
    path("new_co", views.new_co, name="new_co"),
    path("new_inv", views.new_inv, name="new_inv"),
]
