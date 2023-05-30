from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("<h1>Bienvenue sur le blog")


def accueil(request):
    return render(request, "blog/index.html", context={"date": datetime.today()})
