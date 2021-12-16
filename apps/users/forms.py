from django.forms import ModelForm, fields, models
from django.contrib.auth.models import User
from apps.users.models import Data

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password']

class RegisterForm2(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        exclude = ('user', )
