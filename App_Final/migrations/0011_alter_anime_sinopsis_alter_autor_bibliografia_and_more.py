# Generated by Django 4.1 on 2022-09-26 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Final', '0010_remove_imagen_anime_delete_mensaje_delete_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='sinopsis',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='autor',
            name='bibliografia',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='genero',
            name='detalle',
            field=models.TextField(),
        ),
    ]