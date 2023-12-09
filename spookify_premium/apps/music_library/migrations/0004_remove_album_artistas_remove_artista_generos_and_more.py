# Generated by Django 5.0 on 2023-12-09 04:47

import apps.music_library.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0003_rename_song_cancion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artistas',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='generos',
        ),
        migrations.RemoveField(
            model_name='cancion',
            name='artistas',
        ),
        migrations.RemoveField(
            model_name='cancion',
            name='generos',
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artista', to='music_library.artista'),
        ),
        migrations.AddField(
            model_name='cancion',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to=apps.music_library.models.file_path),
        ),
        migrations.AlterField(
            model_name='artista',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cancion',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.music_library.models.file_path),
        ),
    ]