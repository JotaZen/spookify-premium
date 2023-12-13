from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return redirect('/biblioteca/musica')
    return render(request, 'inicio.html')


def view_404(request, exception=None):
    return redirect('/')
