from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name = models.TextField(blank=False, null=False)
    creation_date = models.DateField(auto_created=True)
    logo = models.ImageField(upload_to="LogoTeams", null=True)

class TeamUser(models.Model):
    user = models.ForeignKey(User, models.PROTECT, blank=False, null=False)
    team = models.ForeignKey(Team, models.CASCADE, blank=False, null=False)
    post = models.TextField(blank=False, null=False)

 