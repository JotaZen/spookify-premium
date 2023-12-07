from django.db import models

# Create your models here.


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='artistas', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Album(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='albumes', null=True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
