from django.shortcuts import render, redirect
from ..models import Album
from ..forms import CrearAlbumFormulario
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from ..filtros import FiltroAlbumes

BASE_FOLDER = 'paginas/biblioteca/albumes'
REDIRECT = '/biblioteca/albumes'


@permission_required('music_library.view_album', login_url='login')
def lista_albumes(request):

    albumes = Album.objects.all()
    filtro = FiltroAlbumes()

    if request.method == 'POST':
        filtro = FiltroAlbumes(request.POST)
        nombre = request.POST.get('nombre', None)
        artista = request.POST.get('artista', None)

        if nombre:
            albumes = albumes.filter(nombre__icontains=nombre)

        if artista:
            albumes = albumes.filter(artista__id=artista)

    paginacion = Paginator(albumes, 4).get_page(request.GET.get('pagina'))

    data_template = {
        'albumes': paginacion,
        'filtro': filtro,
    }

    return render(request, f"{BASE_FOLDER}/lista.html", data_template)


@permission_required('music_library.add_album', login_url='login')
def crear_album(request):

    formulario = CrearAlbumFormulario()

    if request.method == 'POST' and request.FILES.get('logo', None):
        formulario = CrearAlbumFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Álbum creado correctamente')

    data_template = {
        'titulo': 'Agregar Álbum',
        'formularioGenerico': formulario,
        'redirect_url': REDIRECT,
    }

    return render(request, "components/formDjangoGenerico.html", data_template)


@permission_required('music_library.change_album', login_url='login')
def editar_album(request, id):

    album = Album.objects.get(id=id)
    formulario = CrearAlbumFormulario(instance=album)

    if request.method == 'POST':
        formulario = CrearAlbumFormulario(
            request.POST, request.FILES, instance=album)

        if formulario.is_valid():

            if album.logo and request.FILES.get('logo', None):
                album.logo.delete()

            formulario.save()
            messages.success(request, 'Álbum editado')

    data_template = {
        'titulo': 'Editar Artista',
        'formularioGenerico': formulario,
        'redirect_url':  REDIRECT,
    }

    return render(request, "components/formDjangoGenerico.html", data_template)


@permission_required('music_library.delete_album', login_url='login')
def eliminar_album(request, id):

    album = album.objects.get(id=id)

    if album.logo:
        album.logo.delete()

    album.delete()

    return redirect(REDIRECT)
