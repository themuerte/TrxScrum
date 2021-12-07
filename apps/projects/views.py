from django.shortcuts import render, redirect
from django.contrib.auth import *

# Create your views here.

def index(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'projects/index.html', queryset)

    elif request.method == "POST":
        pass

def my_projects(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'projects/myProjects.html', queryset)
    
    elif request.method == "POST":
        pass

def my_teams(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'projects/myTeams.html', queryset)
    
    elif request.method == "POST":
        pass

