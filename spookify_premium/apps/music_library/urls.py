from django.urls import path
from .views import viewBusqueda, crearCancion, listaCanciones, jsonTodo

urlpatterns = [
    path('musica/busqueda',  viewBusqueda, name="musica.busqueda"),
    path('musica/agregar',  crearCancion, name="musica.agregar"),
    path('musica/lista',  listaCanciones, name="musica.lista"),
    path('musica/todo',  jsonTodo, name="musica.todo"),
]
