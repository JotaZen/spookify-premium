from .models import Cancion, Artista, Album, Genero
from django import forms


class FiltroCanciones(forms.Form):
    artista = forms.ModelChoiceField(queryset=Artista.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'artista_cancion'}))

    album = forms.ModelChoiceField(queryset=Album.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'album_cancion'}))

    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'genero_cancion'}))

    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark no-placeholder', 'id': 'nombre_cancion'}))


class FiltroArtistas(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark no-placeholder', 'id': 'nombre_artista'}))


class FiltroAlbumes(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark no-placeholder', 'id': 'nombre_album'}))
    artista = forms.ModelChoiceField(queryset=Artista.objects.all(), required=False, widget=forms.Select(
        attrs={'class': 'form-control input-dark', 'id': 'artista_album'}))


class FiltroGeneros(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control input-dark no-placeholder', 'id': 'nombre_genero'}))
