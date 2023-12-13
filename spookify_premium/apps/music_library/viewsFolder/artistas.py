from django.shortcuts import render, redirect
from ..models import Artista
from ..forms import CrearArtistaFormulario
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from ..filtros import FiltroArtistas
BASE_FOLDER = 'paginas/biblioteca/artistas'
REDIRECT = '/biblioteca/artistas'


@permission_required('music_library.view_artista', login_url='login')
def lista_artistas(request):

    artistas = Artista.objects.all()
    filtro = FiltroArtistas()

    if request.method == 'POST':
        filtro = FiltroArtistas(request.POST)
        nombre = request.POST.get('nombre', None)
        if nombre:
            artistas = artistas.filter(nombre__icontains=nombre)

    pagina = request.GET.get('pagina')

    paginacion = Paginator(artistas, 4).get_page(pagina)

    data_template = {
        'artistas': paginacion,
        'filtro': filtro,
    }

    return render(request, f"{BASE_FOLDER}/lista.html", data_template)


@permission_required('music_library.add_artista', login_url='login')
def crear_artista(request):

    formulario = CrearArtistaFormulario()

    if request.method == 'POST' and request.FILES.get('logo', None):
        formulario = CrearArtistaFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Artista creado')

    data_template = {
        'titulo': 'Agregar Artista',
        'formularioGenerico': formulario,
        'redirect_url': REDIRECT,
    }

    return render(request, "components/formDjangoGenerico.html", data_template)


@permission_required('music_library.change_artista', login_url='login')
def editar_artista(request, id):

    artista = Artista.objects.get(id=id)
    formulario = CrearArtistaFormulario(instance=artista)

    if request.method == 'POST':
        formulario = CrearArtistaFormulario(
            request.POST, request.FILES, instance=artista)

        if formulario.is_valid():
            if artista.logo and request.FILES.get('logo', None):
                artista.logo.delete()

            formulario.save()
            messages.success(request, 'Artista editado')

    data_template = {
        'titulo': 'Editar Artista',
        'formularioGenerico': formulario,
        'redirect_url': REDIRECT,
    }

    return render(request, "components/formDjangoGenerico.html", data_template)


@permission_required('music_library.delete_artista', login_url='login')
def eliminar_artista(request, id):

    artista = Artista.objects.get(id=id)

    if artista.logo:
        artista.logo.delete()

    artista.delete()

    return redirect(REDIRECT)
