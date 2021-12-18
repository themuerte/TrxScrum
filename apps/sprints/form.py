from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Sprint, TaskSprint, TaskSprintUser

from apps.projects.models import Role, ProductBacklog, Project


class SprintForm(ModelForm):
    class Meta:
        model = Sprint
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = TaskSprint
        fields = '__all__'    