from django.shortcuts import render
from .models import NewsClip
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!")


def Home(TemplateView):
    template_name = "newsapp/home.html"


def newsclip(request):
    newsclips = NewsClip.objects.all()
    context = {"newsclips": newsclips}
    return render(request, "newsapp/for.html", context)


def allauth(request):
    return render(request, "newsapp/allauth.html")
