from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="login"),
    path("register/", views.register, name="register"),
]