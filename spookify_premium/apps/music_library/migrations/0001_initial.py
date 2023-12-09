# Generated by Django 5.0 on 2023-12-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/artistas')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
                'db_table': 'biblioteca_artistas',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/generos')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Generos',
                'db_table': 'biblioteca_generos',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/albumes')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('artistas', models.ManyToManyField(related_name='albumes', to='music_library.artista')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albumes',
                'db_table': 'biblioteca_albumes',
            },
        ),
        migrations.AddField(
            model_name='artista',
            name='generos',
            field=models.ManyToManyField(related_name='artistas', to='music_library.genero'),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/canciones')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
                ('albumes', models.ManyToManyField(related_name='canciones', to='music_library.album')),
                ('artistas', models.ManyToManyField(related_name='canciones', to='music_library.artista')),
                ('generos', models.ManyToManyField(related_name='canciones', to='music_library.genero')),
            ],
            options={
                'verbose_name': 'Canción',
                'verbose_name_plural': 'Canciones',
                'db_table': 'biblioteca_canciones',
            },
        ),
    ]