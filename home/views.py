from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = ...
    return render(request, 'home/index.html')

def todo(request):
    context = ...
    return render(request, 'home/todo.html')