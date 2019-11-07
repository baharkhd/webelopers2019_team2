# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate

# Create your views here.
from django.urls import path

from edusys.forms import SignUpForm


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
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # password1 = form.cleaned_data.get('password1')
            # password2 = form.cleaned_data.get('password2')
            # user = User.objects.create_user(username, email, password1)
            # user2 = User
            # user.password2 = password2
            # user.last_name = last_name
            # user.first_name = first_name
            # user.save()
        else:
            return HttpResponse(form.errors)
    else:
        return HttpResponse('salam salam')

    return render(request, 'register.html')
