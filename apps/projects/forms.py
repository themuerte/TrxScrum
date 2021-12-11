from django.forms import ModelForm, fields, models
from apps.projects.models import *


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('user', )