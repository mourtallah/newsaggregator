from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newsclip', views.newsclip, name='newsclip'),
    path('allauth', views.allauth, name='allauth'),
]