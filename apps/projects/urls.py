from django.urls import path
from . import views
from .views import CreateView

urlpatterns = [
    path("home/", views.home, name="home"),
    path("my_projects/", views.my_projects, name="my_projects"),
    path("create_project/", CreateView.as_view(), name="create_project"),
]