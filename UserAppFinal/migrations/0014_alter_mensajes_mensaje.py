# Generated by Django 4.1 on 2022-10-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAppFinal', '0013_alter_mensajes_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='mensaje',
            field=models.TextField(),
        ),
    ]
