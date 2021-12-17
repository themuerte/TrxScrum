from django.urls import path
from . import views
from .views import ListTeams, CreateTeam, TeamUpdateView, TeamDeleteView, TeamDetailView, TeamUserCreateView
urlpatterns = [
    path("my_teams",ListTeams.as_view(template_name="teams/myTeams.html"), name="my_teams" ),
    path("create_team", CreateTeam.as_view(template_name="teams/team_form.html"), name="create_team"),
    path("update_team/<int:pk>", TeamUpdateView.as_view(template_name="teams/team_form.html"), name="update_team"),
    path("delete_team/<int:pk>", TeamDeleteView.as_view(), name="delete_team"),
    path("detail_team/<int:pk>", TeamDetailView.as_view(), name="detail_team"),
    path("add_member_team/<int:pk>", TeamUserCreateView.as_view(), name="add_member_team"),
]