# Generated by Django 5.0.3 on 2024-06-10 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_baihat_link_baihat_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baihat',
            old_name='file',
            new_name='audio',
        ),
    ]