from django.http import HttpResponse
import requests
from django.shortcuts import render


def home(request):
    return render(request,"home.html")