# Generated by Django 5.0.3 on 2024-06-15 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_quangcao_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chude',
            name='image',
        ),
    ]
