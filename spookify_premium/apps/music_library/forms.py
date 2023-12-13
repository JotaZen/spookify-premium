from django import forms
from .models import Cancion, Artista, Album, Genero


class CrearCancionFormulario(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = [
            'nombre',
            'descripcion',
            'logo',
            'archivo',
            'album',
            'genero'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control input-dark ', 'id': 'nombre_cancion'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control input-dark', 'id': 'descripcion_cancion'}),
            'logo': forms.FileInput(attrs={'class': 'form-control input-dark', 'accept': 'image/*', 'id': 'logo_cancion'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control input-dark', 'accept': 'audio/mp3, audio/wav, audio/ogg , audio/mpeg',
                                              'id': 'archivo_cancion'}),
            'album': forms.Select(attrs={'class': 'form-control input-dark', 'id': 'album_cancion'}),
            'genero': forms.Select(attrs={'class': 'form-control input-dark', 'id': 'genero_cancion'}),
        }


class CrearArtistaFormulario(forms.ModelForm):
    class Meta:
        model = Artista
        fields = [
            'nombre',
            'descripcion',
            'logo',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control input-dark ', 'id': 'nombre_artista'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control input-dark', 'id': 'descripcion_artista'}),
            'logo': forms.FileInput(attrs={'class': 'form-control input-dark', 'accept': 'image/*', 'id': 'logo_artista'}),
        }


class CrearAlbumFormulario(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'nombre',
            'descripcion',
            'logo',
            'artista',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control input-dark', 'id': 'nombre_album'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control input-dark', 'id': 'descripcion_album'}),
            'logo': forms.FileInput(attrs={'class': 'form-control input-dark', 'accept': 'image/*', 'id': 'logo_album'}),
            'artista': forms.Select(attrs={'class': 'form-control input-dark', 'id': 'artista_album'}),
        }


class CrearGeneroFormulario(forms.ModelForm):
    class Meta:
        model = Genero
        fields = [
            'nombre',
            'descripcion',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control input-dark ', 'id': 'nombre_genero'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control input-dark', 'id': 'descripcion_genero'}),
        }
