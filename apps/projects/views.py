from django.shortcuts import render, redirect
from django.contrib.auth import *

# Create your views here.

def index(request):
    if request.method == "GET":
        queryset = {}
        return render(request, 'projects/index.html', queryset)

    elif request.method == "POST":
        pass
