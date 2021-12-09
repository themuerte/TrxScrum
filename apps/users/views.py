from django.http.request import QueryDict
from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from apps.users.forms import RegisterForm, RegisterForm2
from apps.users.models import Data

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
        form2 = RegisterForm2()
        queryset = {
            'form':form,
            'form2': form2,
        }

        return render(request, 'users/register.html', queryset)

    elif request.method == "POST":

        form = RegisterForm(request.POST)
        form2 = RegisterForm2(request.POST, request.FILES)

        if form.is_valid() and form2.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            data = Data.objects.create(user=user, **form2.cleaned_data)
            data.save()
        else:
            print("error!!")
            print(request.POST)
            print(form.errors)
            print(form2.errors)

        print("POST method")
        return redirect("login")

def profile(request):
    if request.method == "GET":
        queryset = {} #aqui deberia cambiar los datos del usuario
        return render(request, 'users/profile.html', queryset)