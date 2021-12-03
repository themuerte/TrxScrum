from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from apps.users.forms import RegisterForm

# Create your views here.

def index(request):
    form = AuthenticationForm()
    queryset = {
        'form':form
    }

    return render(request,'users/login.html', queryset)

def register(request):
    form = RegisterForm()
    queryset = {
        'form':form
    }

    return render(request, 'users/register.html', queryset)

def reg(request):
    pass