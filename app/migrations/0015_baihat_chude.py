# Generated by Django 5.0.3 on 2024-06-16 19:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_casi_album_casi_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='baihat',
            name='chude',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='baihats', to='app.chude', verbose_name='Chủ đề'),
            preserve_default=False,
        ),
    ]
