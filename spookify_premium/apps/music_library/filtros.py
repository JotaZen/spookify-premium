from .models import Cancion, Artista, Album, Genero
from django import forms


class FiltroCanciones(forms.Form):
    artista = forms.ModelChoiceField(queryset=Artista.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'artista_cancion'}), empty_label='Todos los artistas')

    album = forms.ModelChoiceField(queryset=Album.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'album_cancion'}), empty_label='Todos los álbumes')

    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'genero_cancion'}), empty_label='Todos los géneros')

    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark', 'id': 'nombre_cancion', 'placeholder': 'Título'}), empty_value='')


class FiltroArtistas(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark', 'id': 'nombre_artista', 'placeholder': 'Nombre del artista'}))


class FiltroAlbumes(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark', 'id': 'nombre_album', 'placeholder': 'Nombre del álbum'}))
    artista = forms.ModelChoiceField(queryset=Artista.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'artista_album'}), empty_label='Todos los artistas')


class FiltroGeneros(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark', 'id': 'nombre_genero', 'placeholder': 'Nombre del género'}))
