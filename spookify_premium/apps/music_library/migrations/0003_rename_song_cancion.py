# Generated by Django 5.0 on 2023-12-08 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0002_remove_song_albumes_song_album'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Song',
            new_name='Cancion',
        ),
    ]
