from django.db import models
from django.db.models import fields
from django.forms import forms
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from .models import Team, TeamUser
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import Teamsform, TeamUserForm


# Create your views here.

""" def my_teams(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'teams/myTeams.html', queryset)
    
    elif request.method == "POST":
        pass
 """

class ListTeams(ListView):
    model = Team

class CreateTeam(CreateView):
    model = Team
    fields = ['name','logo','is_active']
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(CreateTeam, self).form_valid(form)

class TeamUpdateView(UpdateView):
    model = Team
    fields = ['name','logo','is_active']
    success_url = reverse_lazy("my_teams")

class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy("my_teams")

class TeamDetailView(DetailView):
    model = Team

class TeamUserCreateView(CreateView):
    model = TeamUser
    template_name = "teams/team_user_form.html"
    #fields = ['user','post','state']
    form_class = TeamUserForm
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super(TeamUserCreateView, self).get_form_kwargs()
        kwargs['team'] = self.request.team.pk
        return kwargs

"""     def form_valid(self, form):
        obj = form.save(commit=False)
        obj.team = self.request.team
        return super(TeamUserCreateView, self).form_valid(form)
     """
    




