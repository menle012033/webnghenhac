# Generated by Django 5.0.3 on 2024-05-29 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_album_chude_playlist_sanpham_category_baihat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yeuthichnhieu',
            name='sampham',
        ),
        migrations.RemoveField(
            model_name='thongtinnguoimua',
            name='khachhang',
        ),
        migrations.RemoveField(
            model_name='thongtinnguoimua',
            name='yeuthich',
        ),
        migrations.RemoveField(
            model_name='yeuthich',
            name='khachhang',
        ),
        migrations.RemoveField(
            model_name='yeuthichnhieu',
            name='yeuthich',
        ),
        migrations.DeleteModel(
            name='Sanpham',
        ),
        migrations.DeleteModel(
            name='Thongtinnguoimua',
        ),
        migrations.DeleteModel(
            name='Yeuthich',
        ),
        migrations.DeleteModel(
            name='Yeuthichnhieu',
        ),
    ]
