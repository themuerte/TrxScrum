from django.forms import ModelForm, fields, models
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
