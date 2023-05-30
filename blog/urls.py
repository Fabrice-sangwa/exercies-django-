from django.urls import path

from .views import index, accueil, articles

urlpatterns = [
    path('', index),
    path('accueil/', accueil),
    path('article-<str:numero_article>/', articles)

]