# Generated by Django 4.1 on 2022-09-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Final', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='imagen_del_anime',
            field=models.ImageField(upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen_anime',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
