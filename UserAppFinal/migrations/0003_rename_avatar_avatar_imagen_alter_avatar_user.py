# Generated by Django 4.1 on 2022-09-19 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserAppFinal', '0002_rename_imagen_avatar_avatar_alter_avatar_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='avatar',
            new_name='imagen',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
