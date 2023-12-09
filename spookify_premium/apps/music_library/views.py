from django.shortcuts import render

# Create your views here.
TEMPLATES = 'paginas/biblioteca'


def viewBusqueda(request):
    return render(request, f'{TEMPLATES}/buscar.html')
