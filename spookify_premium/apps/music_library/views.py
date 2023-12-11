from django.shortcuts import render
from .forms import CrearCancionFormulario
from .models import Cancion
from django.http import JsonResponse
from django.core import serializers
import json

TEMPLATES = 'paginas/biblioteca'


def viewBusqueda(request):
    return render(request, f'{TEMPLATES}/buscar.html')


def crearCancion(request):
    formulario = CrearCancionFormulario()

    data = {
        'form': formulario
    }

    return render(request, f'{TEMPLATES}/musica/agregar.html', data)


def listaCanciones(request):
    canciones = Cancion.objects.all()

    data = {
        'canciones': canciones
    }

    return render(request, f'{TEMPLATES}/musica/lista.html', data)


def jsonTodo(request):

    canciones = Cancion.objects.all()
    canciones_data = []

    for cancion in canciones:
        # Serializar la canción y convertir a diccionario
        cancion_data = serializers.serialize('python', [cancion])[0]['fields']

        # Obtener información del álbum
        album_info = {
            'album': {
                # Ajusta esto según la estructura de tu modelo Album
                'nombre': cancion.album.nombre,
                # Agrega más campos del álbum si es necesario
            }
        }

        # Obtener información del artista
        artista_info = {
            'artista': {
                # Ajusta esto según la estructura de tu modelo Artista
                'nombre': cancion.album.artista.nombre,
                # Agrega más campos del artista si es necesario
            }
        }
        cancion_data['id'] = cancion.id
        cancion_data['archivo'] = cancion.archivo.url if cancion.archivo else None
        cancion_data['logo'] = cancion.logo.url if cancion.logo else None
        # Combinar la información de la canción, álbum y artista
        cancion_data.update(album_info)
        cancion_data.update(artista_info)

        # Agregar la información de la canción a la lista
        canciones_data.append(cancion_data)

    return JsonResponse({'canciones': canciones_data})
