from enum import Flag
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.db.models.fields.related import RelatedField
from apps.teams.models import Team 

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, models.PROTECT, blank=False, null=False, related_name="projects",verbose_name="Usuario")
    team = models.ForeignKey(Team, models.PROTECT, blank=False, null=False, verbose_name="Equip")
    name = models.TextField(blank=False, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    cost = models.DecimalField(max_digits=20, decimal_places=2, null=True,verbose_name="Costo")
    creation_date = models.DateField(auto_now_add=True, verbose_name="Creacion del equipo")
    notes = models.TextField(blank=True, verbose_name="Notas")
    project = models.TextField(blank=True, verbose_name="Tipo de projecto")
    state = models.CharField(max_length=40, blank=False, verbose_name="Estado del proyecto")
    is_active = models.BooleanField(default=True, verbose_name="¿Equipo activo?")

class Role(models.Model):
    user = models.ForeignKey(User, models.PROTECT, blank=False, null=False, verbose_name="Usuario", related_name="user")
    project = models.ForeignKey(Project, models.PROTECT, blank=False, null=False, verbose_name="Proyecto", related_name="roles")
    role = models.CharField(max_length=40, blank=False, null=False, verbose_name="Rol en el proyecto")


class ProductBacklog(models.Model):
    priority_choices = [
        ('HI', 'High'),
        ('ME', 'Mdium'),
        ('LO', 'Low')
    ]
    
    project = models.ForeignKey(Project, models.PROTECT, blank=False, null=False, verbose_name="Proyecto")
    short_story = models.TextField(blank=False, verbose_name="Historia corta")
    state = models.CharField(max_length=20, blank=False, null=False, verbose_name="Estado")
    effort = models.IntegerField(blank=False, verbose_name="Esfuerzo")
    priority = models.CharField(max_length=5, choices=priority_choices, blank=False, verbose_name="Prioridad")