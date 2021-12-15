from django.urls import path
from . import views
from .views import ProjectCreation, ProjectListView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path("home/", views.home, name="home"),
    path("my_projects/", ProjectListView.as_view(), name="my_projects"),
    path("create_project/", ProjectCreation.as_view(), name="create_project"),
    path("update_project/<int:pk>", ProjectUpdateView.as_view(template_name="projects/project_form.html"), name="update_project"),
    path("delete_project/<int:pk>", ProjectDeleteView.as_view(), name="delete_project"),
    path("detail_project/<int:pk>", ProjectDetailView.as_view(), name="detail_project"),
]