from django.shortcuts import render
from .forms import CrearCancionFormulario


TEMPLATES = 'paginas/biblioteca'


def viewBusqueda(request):
    return render(request, f'{TEMPLATES}/buscar.html')


def crearCancion(request):
    formulario = CrearCancionFormulario()

    data = {
        'form': formulario
    }

    return render(request, f'{TEMPLATES}/musica/agregar.html', data)
