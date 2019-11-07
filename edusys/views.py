# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import path


def navbar(request):
    return render(request, 'homepage.html')


def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    return render(request, 'register.html')
