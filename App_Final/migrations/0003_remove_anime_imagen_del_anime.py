# Generated by Django 4.1 on 2022-09-17 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Final', '0002_alter_anime_imagen_del_anime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='imagen_del_anime',
        ),
    ]
