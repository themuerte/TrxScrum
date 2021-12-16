from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.projects.models import Project, ProductBacklog, Role
from apps.projects.forms import ProjectForm

from apps.teams.models import Team

# Create your views here.

def home(request):
    if request.method == "GET":
        queryset = {
            'projects': Project.objects.filter(Q(user=request.user)|Q(roles__user=request.user)),
            'teams': Team.objects.filter(Q(user=request.user)|Q(team_userT__user=request.user))
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

class ProjectListView(ListView):
    model = Project
    template_name = "projects/myProjects.html"

class ProjectCreation(CreateView):
    model = Project
    template_name = 'projects/project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy("home")
    
    def get_form_kwargs(self):
        kwargs = super(ProjectCreation, self).get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        return kwargs
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProjectUpdateView, self).form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(ProjectUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        return kwargs

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("my_projects")
    #no se le pone template por que lo hace por convicion por que es el archivo "project_confirm_delete.html"  osea app_confirm_delete
