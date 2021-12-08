from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name = models.TextField(blank=False, null=False, verbose_name="Nombre")
    creation_date = models.DateField(auto_created=True, verbose_name="Creacion del equipo")
    logo = models.ImageField(upload_to="LogoTeams", null=True)
    is_active = models.BooleanField(default=True, verbose_name="¿Equipo activo?")

class TeamUser(models.Model):
    user = models.ForeignKey(User, models.PROTECT, blank=False, null=False, verbose_name="Usuario")
    team = models.ForeignKey(Team, models.CASCADE, blank=False, null=False, verbose_name="Equipo")
    post = models.TextField(blank=False, null=False, verbose_name="Posición")

 