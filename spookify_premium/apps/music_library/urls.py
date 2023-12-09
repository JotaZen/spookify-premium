from django.urls import path
from .views import viewBusqueda, crearCancion

urlpatterns = [
    path('musica/busqueda',  viewBusqueda, name="musica.busqueda"),
    path('musica/agregar',  crearCancion, name="musica.agregar")
]
