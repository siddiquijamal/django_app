from django.http import HttpResponse
import requests
from django.shortcuts import render
from TODOLISTAPP.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('updated_at')
    data = {
        "tasks" : tasks
    }
    return render(request,"home.html",data)