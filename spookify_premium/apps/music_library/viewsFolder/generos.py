from django.shortcuts import render, redirect
from ..models import Genero
from ..forms import CrearGeneroFormulario
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from ..filtros import FiltroGeneros


BASE_FOLDER = 'paginas/biblioteca/generos'
REDIRECT = '/biblioteca/generos'


@permission_required('music_library.view_genero', login_url='login')
def lista_generos(request):

    generos = Genero.objects.all()
    filtro = FiltroGeneros()

    if request.method == 'POST':
        filtro = FiltroGeneros(request.POST)
        nombre = request.POST.get('nombre', None)

        if nombre:
            generos = generos.filter(nombre__icontains=nombre)

    paginacion = Paginator(generos, 6).get_page(request.GET.get('pagina', 1))

    data_template = {
        'generos': paginacion,
        'filtro': filtro,
    }

    return render(request, f"{BASE_FOLDER}/lista.html", data_template)


@permission_required('music_library.add_genero', login_url='login')
def crear_genero(request):

    formulario = CrearGeneroFormulario()

    if request.method == 'POST':
        formulario = CrearGeneroFormulario(request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Género registrado')

    data_template = {
        'titulo': 'Agregar Género',
        'formularioGenerico': formulario,
        'redirect_url': REDIRECT,
    }

    return render(request, "components/formDjangoGenerico.html", data_template)


@permission_required('music_library.change_genero', login_url='login')
def editar_genero(request, id):

    genero = Genero.objects.get(id=id)
    formulario = CrearGeneroFormulario(instance=genero)

    if request.method == 'POST':
        formulario = CrearGeneroFormulario(request.POST, instance=genero)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Género actualizado')

    data_template = {
        'titulo': 'Editar Género',
        'formularioGenerico': formulario,
        'redirect_url': REDIRECT,
    }

    return render(request, "components/formDjangoGenerico.html", data_template)


@permission_required('music_library.delete_genero', login_url='login')
def eliminar_genero(request, id):

    genero = Genero.objects.get(id=id)

    genero.delete()

    return redirect(REDIRECT)
