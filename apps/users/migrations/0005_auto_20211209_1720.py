# Generated by Django 3.2.9 on 2021-12-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211208_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='logo',
            field=models.ImageField(null=True, upload_to='User logo'),
        ),
        migrations.AlterField(
            model_name='data',
            name='phone',
            field=models.IntegerField(blank=True, verbose_name='Telefono'),
        ),
    ]
