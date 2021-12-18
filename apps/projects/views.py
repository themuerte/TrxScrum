from django.contrib.auth.models import User
from django.db.models import Q, fields
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps import projects

from apps.projects.models import Project, ProductBacklog, Role
from apps.projects.forms import ProjectForm, RoleForm, BacklogForm

from apps.teams.models import Team, TeamUser

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
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProjectCreation, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ProjectCreation, self).get_form_kwargs()
        kwargs['user'] = self.request.user.pk
        return kwargs
    
class ProjectDetailView(DetailView):
    model = Project
    fields = '__all__'
    template_name = "projects/project_detail.html"
""" 
    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        print(context['object'])
        context['team'] = Team.objects.filter(user__pk=self.request.user.pk)
        context['team_user'] = TeamUser.objects.filter(project__pk=context.get('id'))
        context['roles'] = Role.objects.filter(project__pk=self.request.GET.get['pk'])
        
        return context """

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ProjectUpdateView, self).form_valid(form)
    

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("my_projects")
    #no se le pone template por que lo hace por convicion por que es el archivo "project_confirm_delete.html"  osea app_confirm_delete

class RoleCreateView(CreateView):
    model = Role
    form_class = RoleForm
    template_name = "projects/project_role_form.html"
    success_url = reverse_lazy("home")


    def form_valid(self, form):
        obj = form.save(commit=False)
        project = Project.objects.get(pk=self.kwargs['pk'])
        obj.project = project
        return super(RoleCreateView, self).form_valid(form)

class ProductBacklogCreateView(CreateView):
    model = ProductBacklog
    form_class = BacklogForm
    template_name = "projects/projects_backlog_form.html"
    success_url = reverse_lazy("my_projects")
    #success_url = reverse('detail_project', kwargs=[request.GET['pk']]) #si esto no se puede mandarlo al projectlist

    def form_valid(self, form):
        obj = form.save(commit=False)
        project = Project.objects.get(pk=self.kwargs['pk'])
        obj.project = project
        return super(ProductBacklogCreateView, self).form_valid(form)