import datetime

from django.http import HttpResponse
from django.shortcuts import render
from datetime import  datetime


def index(request):
    return HttpResponse("<h1>Salutation</h1>")


def bienvenue(request):
    return render(request, "bienvenue.html")


def data(request):
    return render(request, "data.html", context={"date": datetime.today(), "name" : "fabrice"})
