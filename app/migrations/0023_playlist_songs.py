# Generated by Django 5.0.3 on 2024-06-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_theloai_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='playlists', to='app.playlist'),
        ),
    ]
