from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views
from .views import CreateView

urlpatterns = [
    path("home/", views.home, name="home"),
    path("my_projects/", views.my_projects, name="my_projects"),
    path("my_teams/", views.my_teams, name="my_teams"),
    path("create_project/", CreateView.as_view(), name="create_project")
]