from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("<h1>Bienvenue sur le blog")


def accueil(request):
    return render(request, "blog/index.html", context={"date": datetime.today()})


def articles(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, "blog/not_found.html")