from django.shortcuts import render

# Create your views here.
from django.urls import path


def navbar(request):
    return render(request, 'base.html')
