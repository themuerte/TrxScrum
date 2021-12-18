from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from .views import SprintCreateView, TaskSprintCreateView

urlpatterns = [
    path("sprint_add", SprintCreateView.as_view(), name="sprint_add"),
    path("task_add", TaskSprintCreateView.as_view(), name="task_add"),
]