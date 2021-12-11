from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Data(models.Model):
    #hacer la llave foreana para el dato del telefono 
    user = models.OneToOneField(User, models.PROTECT, blank=False, null=False, related_name="data",verbose_name="Usuario")
    phone = models.IntegerField(blank=True, verbose_name="Telefono")
    logo = models.ImageField(upload_to="UserImages", null=True)


