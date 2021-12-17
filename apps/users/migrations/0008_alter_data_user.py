# Generated by Django 4.0 on 2021-12-16 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0007_alter_data_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='auth.user', verbose_name='Usuario'),
        ),
    ]