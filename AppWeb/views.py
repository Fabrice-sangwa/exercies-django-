from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Salutation</h1>")


def bienvenue(request):
    return render(request, "bienvenue.html")
