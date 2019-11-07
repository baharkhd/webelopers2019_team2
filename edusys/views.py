# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate

# Create your views here.
from django.urls import path

from edusys.forms import SignUpForm, LoginForm


def navbar(request):
    return render(request, 'homepage.html')


def homepage(request):
    return render(request, 'homepage.html')


def enter_register(request):
    return render(request, 'register.html')


def login_form(request):
    return render(request, 'login.html')


def login_page(request):
    error = ''
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        error = "error"
    return render(request, 'homepage_login.html', {'error': error})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
    return render(request, 'register.html')
