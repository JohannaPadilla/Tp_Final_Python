# Generated by Django 4.1 on 2022-09-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Final', '0006_alter_anime_titulo_alter_autor_nombre_editorial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='autor',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anime',
            name='genero',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]