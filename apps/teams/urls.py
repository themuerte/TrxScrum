from django.urls import path
from . import views

urlpatterns = [
    path("my_teams/", views.my_teams, name="my_teams"),
]