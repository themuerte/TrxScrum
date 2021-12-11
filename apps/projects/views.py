from django.contrib.auth.forms import AdminPasswordChangeForm
from django.db.models import fields
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.projects import forms

from apps.projects.models import Project, ProductBacklog, Role
from apps.users.models import Data


# Create your views here.

def home(request):
    if request.method == "GET":
        queryset = {
        }
        return render(request, 'projects/index.html', queryset)

    elif request.method == "POST":
        pass

def my_projects(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'projects/myProjects.html', queryset)
    
    elif request.method == "POST":
        pass

#mirar si cambiar esta vista a la apps de teams
def my_teams(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'projects/myTeams.html', queryset)
    
    elif request.method == "POST":
        pass

class ProjectCreation(CreateView):
    model = Project
    success_url = reverse_lazy("home")
    template_name = 'projects/create_project.html'
    exclude = ('user', )

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProjectCreation, self).form_valid(form)

