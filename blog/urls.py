from django.urls import path

from .views import index, accueil

urlpatterns = [
    path('', index),
    path('accueil/', accueil)

]