# Generated by Django 3.2.9 on 2021-12-06 23:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_rename_telefono_datos_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Datos',
            new_name='Data',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='usuario',
            new_name='user',
        ),
    ]