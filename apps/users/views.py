from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from apps.users.forms import RegisterForm

# Create your views here.

def login(request):
    
    if request.method == "GET":
        form = AuthenticationForm()
        queryset = {
            'form':form
        }
        return render(request,'users/login.html', queryset)
    
    elif request.method == "POST":
        pass
    
    

def register(request):
    
    if request.method == "GET":
        form = RegisterForm()
        queryset = {
            'form':form
        }

        return render(request, 'users/register.html', queryset)

    elif request.method == "POST":
        pass
