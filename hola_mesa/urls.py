from django.urls import path
from .views import hola

urlpath = [
    path('', hola)
]