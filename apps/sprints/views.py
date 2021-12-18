from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Sprint, TaskSprintUser, TaskSprint
from .form import SprintForm, TaskForm

# Create your views here.

class SprintCreateView(CreateView):
    model = Sprint
    template_name = "sprints/sprint_form.html"
    form_class = SprintForm

    def get_success_url(self):
        return reverse('detail_project', args=[self.object.product_backlog.project.id]) 

class TaskSprintCreateView(CreateView):
    model = TaskSprint
    template_name = "sprints/task_form.html"
    form_class = TaskForm

    def get_success_url(self):
        return reverse('detail_project', args=[self.object.sprint.product_backlog.project.id]) 
    
