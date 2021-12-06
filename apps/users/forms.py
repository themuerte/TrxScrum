from django.forms import ModelForm, fields, models
from django.contrib.auth.models import User
from apps.users.models import Datos


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password',]
