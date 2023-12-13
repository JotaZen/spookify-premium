from django.urls import path
from .viewsFolder.canciones import viewBusqueda, crearCancion, jsonTodo, index

urlpatterns = [
    path('musica/busqueda',  viewBusqueda, name="musica.busqueda"),
    path('musica/agregar',  crearCancion, name="musica.agregar"),
    path('musica/',  index, name="musica.lista"),
    path('musica/todo',  jsonTodo, name="musica.todo"),
]
