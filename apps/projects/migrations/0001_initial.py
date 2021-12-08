# Generated by Django 3.2.9 on 2021-12-08 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_created=True, verbose_name='Creacion del equipo')),
                ('name', models.TextField(verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Costo')),
                ('notes', models.TextField(blank=True, verbose_name='Notas')),
                ('project', models.TextField(blank=True, verbose_name='Tipo de projecto')),
                ('state', models.CharField(max_length=40, verbose_name='Estado del proyecto')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Equipo activo?')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.team', verbose_name='Equip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=40, verbose_name='rol en el proyecto')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project', verbose_name='proyecto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ProductBacklog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_story', models.TextField(verbose_name='Historia corta')),
                ('state', models.CharField(max_length=20, verbose_name='Estado')),
                ('effort', models.IntegerField(verbose_name='Esfuerzo')),
                ('priority', models.CharField(choices=[('HI', 'High'), ('ME', 'Mdium'), ('LO', 'Low')], max_length=5, verbose_name='Prioridad')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project', verbose_name='proyecto')),
            ],
        ),
    ]