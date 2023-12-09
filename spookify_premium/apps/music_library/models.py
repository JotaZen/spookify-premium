from django.db import models

# Create your models here.


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/generos', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Generos'
        db_table = 'biblioteca_generos'


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/artistas', null=True, blank=True)
    generos = models.ManyToManyField(Genero, related_name='artistas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        db_table = 'biblioteca_artistas'


class Album(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='logos/albumes', null=True, blank=True)
    artistas = models.ManyToManyField(Artista, related_name='albumes')
    # generos = models.ManyToManyField(Genero, related_name='albumes')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albumes'
        db_table = 'biblioteca_albumes'

    def get_canciones(self):
        canciones_activas = self.canciones.filter(activo=True)
        return canciones_activas


class Cancion(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    logo = models.ImageField(
        upload_to='logos/canciones', null=True, blank=True)
    album = models.ForeignKey(
        Album, related_name='canciones', on_delete=models.CASCADE, null=True, blank=True)
    artistas = models.ManyToManyField(Artista, related_name='canciones')
    generos = models.ManyToManyField(Genero, related_name='canciones')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Canción'
        verbose_name_plural = 'Canciones'
        db_table = 'biblioteca_canciones'
