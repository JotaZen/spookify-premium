from django.urls import path
from .views import viewBusqueda

urlpatterns = [
    path('musica/busqueda',  viewBusqueda, name="musica.busqueda")
]
