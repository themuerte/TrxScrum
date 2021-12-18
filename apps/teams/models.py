from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=False, related_name="teams",verbose_name="Usuario", default="")
    name = models.TextField(blank=False, null=False, verbose_name="Nombre")
    creation_date = models.DateField(auto_now_add=True, verbose_name="Creacion del equipo")
    logo = models.ImageField(upload_to="LogoTeams", blank=True,null=True)
    is_active = models.BooleanField(default=True, verbose_name="¿Equipo activo?")

    def __str__(self):
        return self.name

class TeamUser(models.Model):
    state_choices = [
        ('AC','Active'),
        ('WA', 'Waiting'),
        ('DE', 'Deactivated')
    ]
    
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False, related_name="team_userU",verbose_name="Usuario")
    team = models.ForeignKey(Team, models.CASCADE, blank=False, null=False, related_name="team_userT",verbose_name="Equipo")
    post = models.TextField(blank=False, null=False, verbose_name="Posición")
    state = models.CharField(max_length=2, choices=state_choices, verbose_name="Estado") #cuando se cree su estado sera waiting

    def __str__(self):
        return self.team.name +"- "+ self.user.username +" ("+ self.post + ") " + self.state



 