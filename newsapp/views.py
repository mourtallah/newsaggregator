from django.shortcuts import render
from .models import (
    NewsClip,
    Investor,
    Deal,
    Company,
    DealForm,
    CompanyForm,
    InvestorForm,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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


def new_deal(request):
    if request.method == "POST":
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = Deal()
    return render(request, "newsapp/new_deal.html", {"form": form})


def new_co(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = Company()
    return render(request, "newsapp/new_co.html", {"form": form})


def new_inv(request):
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = Investor()
    return render(request, "newsapp/new_inv.html", {"form": form})


def allauth(request):
    return render(request, "newsapp/allauth.html")
