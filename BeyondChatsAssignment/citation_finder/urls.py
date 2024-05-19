# citation_finder/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.citations, name='citations'),
]
