from django.shortcuts import render, redirect
from ..models import Cancion
from ..forms import CrearCancionFormulario
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
import csv
from ..filtros import FiltroCanciones
from django.contrib import messages
BASE_FOLDER = 'paginas/biblioteca/musica'
REDIRECT = '/biblioteca/musica'


@permission_required('music_library.view_cancion', login_url='login')
def lista_canciones(request):

    canciones = Cancion.objects.all()
    filtro = FiltroCanciones()

    if request.method == 'POST':
        filtro = FiltroCanciones(request.POST)
        nombre = request.POST.get('nombre', None)
        artista = request.POST.get('artista', None)
        album = request.POST.get('album', None)
        genero = request.POST.get('genero', None)

        if nombre:
            canciones = canciones.filter(nombre__icontains=nombre)

        if artista:
            canciones = canciones.filter(album__artista__id=artista)

        if album:
            canciones = canciones.filter(album__id=album)

        if genero:
            canciones = canciones.filter(genero__id=genero)

    pagina = request.GET.get('pagina')

    paginacion = Paginator(canciones, 12).get_page(pagina)

    data = {
        'canciones': paginacion,
        'filtro': filtro,
    }

    return render(request, f"{BASE_FOLDER}/lista.html", data)


@permission_required('music_library.add_cancion', login_url='login')
def view_busqueda(request):
    return render(request, f'paginas/biblioteca/buscar.html')


@permission_required('music_library.add_cancion', login_url='login')
def crear_cancion(request):
    formulario = CrearCancionFormulario()

    if request.method == 'POST' and request.FILES['archivo'] and request.FILES['logo']:
        formulario = CrearCancionFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Canción agregada')

    data = {
        'formularioGenerico': formulario,
        'titulo': 'Agregar Canción',
        'redirect_url': REDIRECT,

    }

    return render(request, f'components/formDjangoGenerico.html', data)


@permission_required('music_library.change_cancion', login_url='login')
def editar_cancion(request, id):
    cancion = Cancion.objects.get(id=id)
    formulario = CrearCancionFormulario(instance=cancion)

    if request.method == 'POST':
        formulario = CrearCancionFormulario(
            request.POST, request.FILES, instance=cancion)

        if formulario.is_valid():
            if cancion.archivo and request.FILES.get('archivo', None):
                cancion.archivo.delete()

            if cancion.logo and request.FILES.get('logo', None):
                cancion.logo.delete()

            formulario.save()
            messages.success(request, 'Canción editada')

    data = {
        'formularioGenerico': formulario,
        'titulo': 'Editar Canción',
        'redirect_url': REDIRECT,
    }

    return render(request, f'components/formDjangoGenerico.html', data)


@permission_required('music_library.delete_cancion', login_url='login')
def eliminar_cancion(request, id):
    cancion = Cancion.objects.get(id=id)

    if cancion.archivo:
        cancion.archivo.delete()

    if cancion.logo:
        cancion.logo.delete()

    cancion.delete()
    return redirect(REDIRECT)


@permission_required('music_library.view_cancion', login_url='login')
def json_todo(request):

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


@permission_required('music_library.view_cancion', login_url='login')
def exportar_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="spookify_respaldo.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'nombre', 'artista', 'album',
                    'genero', 'fecha_creacion', 'archivo', 'logo'])
    for cancion in Cancion.objects.all():
        writer.writerow([cancion.id, cancion.nombre, cancion.album.artista.nombre, cancion.album.nombre,
                         cancion.genero, cancion.fecha_creacion, cancion.archivo, cancion.logo])
    return response
