from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.utils.functional import new_method_proxy
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("logout/",  LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name="logout"), #necesita cmabiarse a la pagina que se redirija - mirar lo del redirect
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile")
]