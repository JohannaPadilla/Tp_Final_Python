# Generated by Django 4.1 on 2022-09-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Final', '0004_anime_imagen_del_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='imagen_del_anime',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]