from django.shortcuts import render
from .models import NewsClip, Investor, Deal, Company
from django.http import HttpResponse


def index(request):
    newsclips = NewsClip.objects.all()
    deals = Deal.objects.all()
    companies = Company.objects.all()
    investors = Investor.objects.all()
    context = {
        "newsclips": newsclips,
        "deals": deals,
        "companies": companies,
        "investors": investors,
    }
    return render(request, "newsapp/index.html", context)


def Home(TemplateView):
    template_name = "newsapp/home.html"


def newsclip(request):
    newsclips = NewsClip.objects.all()
    context = {"newsclips": newsclips}
    return render(request, "newsapp/for.html", context)


def deal(request):
    deals = Deal.objects.all()
    context = {"deals": deals}
    return render(request, "newsapp/for.html", context)


def company(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, "newsapp/for.html", context)


def investor(request):
    investors = Investor.objects.all()
    context = {"investors": investors}
    return render(request, "newsapp/for.html", context)


def allauth(request):
    return render(request, "newsapp/allauth.html")
