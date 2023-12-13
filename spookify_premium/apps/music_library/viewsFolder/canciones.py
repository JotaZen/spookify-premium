from django.shortcuts import render
from ..models import Cancion
from ..forms import CrearCancionFormulario
from django.http import JsonResponse
from django.core import serializers

BASE_FOLDER = 'paginas/biblioteca/musica'


def index(request):

    canciones = Cancion.objects.all()

    data = {
        'canciones': canciones
    }

    return render(request, f"{BASE_FOLDER}/lista.html", data)


def viewBusqueda(request):
    return render(request, f'paginas/biblioteca/buscar.html')


def crearCancion(request):
    formulario = CrearCancionFormulario()

    data = {
        'formularioGenerico': formulario,
        'titulo': 'Agregar Canción',
    }

    return render(request, f'components/formDjangoGenerico.html', data)




def jsonTodo(request):

    canciones = Cancion.objects.all()
    canciones_data = []

    for cancion in canciones:
        cancion_data = serializers.serialize('python', [cancion])[0]['fields']

        album_info = {
            'album': {
                'nombre': cancion.album.nombre,
            }
        }

        artista_info = {
            'artista': {
                'nombre': cancion.album.artista.nombre,
            }
        }
        cancion_data['id'] = cancion.id
        cancion_data['archivo'] = cancion.archivo.url if cancion.archivo else None
        cancion_data['logo'] = cancion.logo.url if cancion.logo else None
        cancion_data.update(album_info)
        cancion_data.update(artista_info)

        canciones_data.append(cancion_data)

    return JsonResponse({'canciones': canciones_data})