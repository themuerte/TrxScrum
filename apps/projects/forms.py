from django.forms import ModelForm
from apps.projects.models import *
from apps.teams.models import Team

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['team','name','description','cost','notes','project','state','is_active' ,'creation_date']
        exclude = ('user','creation_date', )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.filter(user__pk=user)