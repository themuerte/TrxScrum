from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Datos(models.Model):
    #hacer la llave foreana para el dato del telefono 
    usuario = models.OneToOneField(User, models.PROTECT, blank=False, null=False)
    phone = models.IntegerField()


