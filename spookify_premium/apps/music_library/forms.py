from django import forms
from .models import Cancion


class CrearCancionFormulario(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = [
            'nombre',
            'descripcion',
            'logo',
            'archivo',
            'album',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control input-dark no-placeholder', 'id': 'nombre_cancion'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control input-dark', 'id': 'descripcion_cancion'}),
            'logo': forms.FileInput(attrs={'class': 'form-control input-dark', 'accept': 'image/*', 'id': 'logo_cancion'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control input-dark', 'accept': 'audio/mp3, audio/wav, audio/ogg , audio/mpeg',
                                              'id': 'archivo_cancion'}),
            'album': forms.Select(attrs={'class': 'form-control input-dark', 'id': 'album_cancion'}),
        }
