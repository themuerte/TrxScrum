from django.db import models
from django.forms import ModelForm, fields
from .models import Team, TeamUser

class Teamsform(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ['user',]

class TeamUserForm(ModelForm):
    class Meta:
        model = TeamUser
        fields = '__all__'
        exclude = ['team',]
        
