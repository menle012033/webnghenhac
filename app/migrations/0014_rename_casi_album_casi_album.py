# Generated by Django 5.0.3 on 2024-06-15 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_artist_name_album_casi_remove_chude_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='casi',
            new_name='casi_album',
        ),
    ]