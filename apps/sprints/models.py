from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeDoneView
from django.db import models
from django.contrib.auth.models import User
from apps.projects.models import ProductBacklog, Project
 
# Create your models here.

class SprintPlannig(models.Model):
    product_backlog = models.ForeignKey(ProductBacklog, models.CASCADE, blank=False, null=False, verbose_name="Product backlog")
    date = models.DateField(blank=False, null=False, verbose_name="Fecha del sprint planning")
    place = models.CharField(max_length=15, blank=False, null=False, verbose_name="Lugar")
    notes = models.TextField(blank=True, verbose_name="Notas")
    observations = models.TextField(blank=True, verbose_name="Observaciones")


class Sprint(models.Model):
    sprint_planning = models.ForeignKey(SprintPlannig, models.CASCADE, blank=False, null=False, verbose_name="Spring planning")
    state = models.CharField(max_length=40, blank=False, verbose_name="Estado del sprint")
    responsable = models.CharField(max_length=10, blank=False, null=False, verbose_name="Responsable del spriint") #regularmente tiene que se el scrum master
    number_sprint = models.IntegerField(blank=True, verbose_name="Numero del sprint")
    start_date = models.DateField(blank=False, null=False, verbose_name="Fecha de inicio")
    end_date = models.DateField(blank=False, null=False, verbose_name="Fecha de finalizacion")
    version = models.CharField(max_length=5, blank=True)

class DailyScrum(models.Model): 
    sprint = models.ForeignKey(Sprint, models.CASCADE, blank=False, null=False, verbose_name="Sprint")
    date = models.DateField(blank=False, null=False, verbose_name="Fecha")
    hour = models.CharField(max_length=10, blank=False, null=False, verbose_name="Hora")
    notes = models.TextField(verbose_name="Notas")
    place = models.CharField(max_length=15, blank=False, null=False, verbose_name="Lugar")

class SprintReview(models.Model):
    sprint = models.ForeignKey(Sprint, models.CASCADE, blank=False, null=False, verbose_name="Sprint")
    date = models.DateField(blank=False, null=False, verbose_name="Fecha") #esta tiene que ser la fecha del final del sprint
    hour = models.CharField(max_length=10, blank=False, null=False, verbose_name="Hora")
    notes = models.TextField(verbose_name="Notas")
    place = models.CharField(max_length=15, blank=False, null=False, verbose_name="Lugar")
    observations = models.TextField(blank=True, verbose_name="Observaciones")
    problems = models.TextField(blank=True, verbose_name="Problemas")

class TaskSprint(models.Model):
    
    state_choices= [
        ('ST', 'Starting'),
        ('PO', 'In progress'),
        ('DE','Detained'),
        ('FI','Finished')

    ]
    sprint = models.ForeignKey(Sprint, models.CASCADE, blank=False, null=False, verbose_name="Sprint")
    name = models.TextField(blank=False, verbose_name="Nombre")
    description = models.TextField(blank=False, null=False, verbose_name="Descripcion")
    points_of_effort = models.IntegerField(blank=False, null=False, verbose_name="Puntos de esfuerzo")
    start_date = models.DateField(blank=False, null=False, verbose_name="Fecha de inicio")
    estimated_end_date = models.DateField(blank=False, null=False, verbose_name="Fecha estimada de finalizacion")
    final_end_date = models.DateField(blank=False, null=False, verbose_name="Fecha de finalizacion")
    observations = models.TextField(blank=True, verbose_name="Observaciones")
    problems_found = models.TextField(blank=True, verbose_name="Problemas")
    state = models.CharField(max_length=5, choices=state_choices, verbose_name="Estado")


class TaskSprintUser(models.Model):
    task_sprinnt = models.ForeignKey(TaskSprint, models.CASCADE, blank=False, null=False, verbose_name="Tareas")
    user = models.ForeignKey(User, models.CASCADE, blank=False, null=False, verbose_name="Usuario")    

class SprintRetrospective(models.Model):
    project = models.ForeignKey(Project, models.CASCADE, blank=False, null=False, verbose_name="Proyecto")
    date = models.DateField(blank=False, null=False, verbose_name="Fecha del sprint retrospective")
    place = models.CharField(max_length=15, blank=False, null=False, verbose_name="Lugar")
    observations = models.TextField(blank=True, verbose_name="Observaciones")