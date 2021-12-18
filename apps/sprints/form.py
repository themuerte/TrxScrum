from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Sprint, TaskSprint, TaskSprintUser

from apps.projects.models import Role, ProductBacklog, Project


class SprintForm(ModelForm):
    class Meta:
        model = Sprint
        fields = ['state','responsable','number_sprint','start_date','end_date','version']
        exclude = ['product_backlog',]