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
        username = request.POST['username']
        password = request.POST['password']

        print('username: '+ username)
        print('password: '+ password)

        user = authenticate(request ,username=username, password=password)

        if user is not None:
            print("esta autenticado")
            return render(request, 'projects/index.html')
        else:
            return redirect('login')

def logout(request):
    
    if request.method=="POST":
        logout(request)
    
    

def register(request):
    
    if request.method == "GET":
        form = RegisterForm()
        queryset = {
            'form':form,
        }

        return render(request, 'users/register.html', queryset)

    elif request.method == "POST":

        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
        else:
            print("error!!")
            print(request.POST)

        print("POST method")
        return redirect("login")
