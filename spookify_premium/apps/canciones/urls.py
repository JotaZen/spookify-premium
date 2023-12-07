
from django.urls import path
from .views import busqueda

urlpatterns = [
    path('', busqueda, name='canciones.busqueda'),
]
