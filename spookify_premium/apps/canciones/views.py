from django.shortcuts import render

# Create your views here.
templateDir = 'paginas/canciones'


def busqueda(request):
    return render(request, f'{templateDir}/buscar.html')
