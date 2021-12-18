from django.db.models import fields
from django.forms import ModelForm
from apps.projects.models import *
from apps.teams.models import Team, TeamUser

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['team','name','description','cost','notes','project','state','is_active' ,'creation_date']
        exclude = ('user','creation_date', )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.filter(user__pk=user)

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = ['user', 'role']
        exclude = ['project',]

class ProjectFormDetail(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProjectFormDetail, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = Team.objects.filter(user__pk=user)
        self.fields['team_user'].queryset = TeamUser.objects.filter(user__pk=user)
        self.fields['roles'].queryset = Role.objects.filter(user__pk=user)

class BacklogForm(ModelForm):
    class Meta:
        model = ProductBacklog
        fields = ['name','short_story','state','effort','priority']
        exclude = ['project',]