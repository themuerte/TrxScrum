from django.http import request
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.contrib.auth import login as login_django
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from apps.users.forms import RegisterForm, RegisterForm2
from apps.users.models import Data

from django.views.generic import UpdateView

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
            login_django(request, user)
            return redirect('home')
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
        return redirect("login_v")


class UserUpdateView(UpdateView):
    model = User
    second_model = Data
    fields = ['username','first_name', 'last_name', 'email']
    template_name = "users/user_form.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        data=Data.objects.get(user=self.request.user.pk)
        context['form2'] = RegisterForm2(initial={'phone':data.phone,'logo':data.logo})
        print(context)
        return context
    
    #mirar lo de sobre escriir el metodo post -> https://stackoverflow.com/questions/48713553/django-updateview-with-multiple-models-and-multiple-forms-dont-work
""" def post(self, request, *args, **kwargs):
       self.object = self.get_object
       user_id = kwargs['pk']
       user = self.model.objects. """
