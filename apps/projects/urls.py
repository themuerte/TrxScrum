from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("my_projects/", views.my_projects, name="my_projects"),
    path("my_teams/", views.my_teams, name="my_teams"),
]