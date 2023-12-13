from django.urls import path
from .viewsFolder.canciones import view_busqueda, eliminar_cancion, editar_cancion, lista_canciones, crear_cancion, json_todo, exportar_data
from .viewsFolder.artistas import lista_artistas, crear_artista, editar_artista, eliminar_artista
from .viewsFolder.albumes import lista_albumes, crear_album, editar_album, eliminar_album
from .viewsFolder.generos import lista_generos, crear_genero, editar_genero, eliminar_genero

urlpatterns = [
    path('musica/busqueda',  view_busqueda, name="musica.busqueda"),
    path('musica/agregar',  crear_cancion, name="musica.agregar"),
    path('musica/editar/<int:id>',  editar_cancion, name="musica.editar"),
    path('musica/eliminar/<int:id>',  eliminar_cancion, name="musica.eliminar"),
    path('musica/',  lista_canciones, name="musica.lista"),
    path('musica/todo',  json_todo, name="musica.todo"),
    path('musica/respaldo',  exportar_data, name="musica.respaldo"),

    path('artistas/',  lista_artistas, name="artistas.lista"),
    path('artistas/agregar',  crear_artista, name="artistas.agregar"),
    path('artistas/editar/<int:id>',  editar_artista, name="artistas.editar"),
    path('artistas/eliminar/<int:id>',
         eliminar_artista, name="artistas.eliminar"),

    path('albumes/',  lista_albumes, name="albumes.lista"),
    path('albumes/agregar',  crear_album, name="albumes.agregar"),
    path('albumes/editar/<int:id>',  editar_album, name="albumes.editar"),
    path('albumes/eliminar/<int:id>',  eliminar_album, name="albumes.eliminar"),

    path('generos/',  lista_generos, name="generos.lista"),
    path('generos/agregar',  crear_genero, name="generos.agregar"),
    path('generos/editar/<int:id>',  editar_genero, name="generos.editar"),
    path('generos/eliminar/<int:id>',  eliminar_genero, name="generos.eliminar"),
]
