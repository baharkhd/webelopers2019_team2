# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate

# Create your views here.
from django.urls import path

from edusys.forms import SignUpForm, LogInForm


def navbar(request):
    return render(request, 'homepage.html')


def homepage(request):
    return render(request, 'homepage.html')


def enter_register(request):
    return render(request, 'register.html')


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

    return render(request, 'register.html')


# def user_login(request):
#     if request.method == 'POST':
#         form = LogInForm()
#         if form.is_valid():
#             # user = form.save()
#             username = form.cleaned_data.get('username')
#             password1 = form.cleaned_data.get('password1')
#             user = authenticate(request, username=username, password1=password1)
#             if user:
#                 pass
#             else:
#                 pass
#         else:




def enter_login(request):
    return render(request, 'login_form.html')


def enter_contact_page(request):
    return render(request, 'contact_form.html')


def submit_contact(request):
    if request.method == "POST":
        pass


def contact_done(request):
    return render(request, 'contact_done.html')