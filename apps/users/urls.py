from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from .views import login, register, UserUpdateView

urlpatterns = [
    path("", login, name="login"),
    path("logout/",  LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"), #necesita cmabiarse a la pagina que se redirija - mirar lo del redirect
    path("register/", register, name="register"),
    path("profile/<int:pk>", UserUpdateView.as_view(), name="profile")
]