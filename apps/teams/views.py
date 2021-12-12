from django.shortcuts import render, redirect
from .models import Team, TeamUser


# Create your views here.

def my_teams(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'teams/myTeams.html', queryset)
    
    elif request.method == "POST":
        pass

def addTeams(request):
    pass