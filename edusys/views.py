# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.conf import settings

# Create your views here.
from django.urls import path

from edusys.forms import SignUpForm, LoginForm, ContactUsForm


def navbar(request):
    return render(request, 'homepage.html', {'file': 'base.html', 'error': ''})


def homepage(request):
    return render(request, 'homepage.html', {'file': 'base.html', 'error': ''})


def enter_register(request):
    return render(request, 'register.html')


def login_form(request):
    return render(request, 'login.html')


def login_page(request):
    error = ""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        error = "error"
    context = {'file': 'none.html', 'error': error}
    return render(request, 'homepage.html', context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
    return render(request, 'register.html')


def enter_contact_us(request):
    return render(request, 'contact_form.html')


def submit_contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            title = form.cleaned_data.get("title")
            text = form.cleaned_data.get("text")
            # if request.user.email == email:
            sendEmail(email, title, text)

            # return render(request, 'contact_done.html')
        else:
            return HttpResponse(form.email)
    return render(request, 'contact_form.html')


def sendEmail(fromEmail, title, text):
    res = send_mail(title, (fromEmail, text), fromEmail, ['webe19lopers@gmail.com', ])
    return HttpResponse('%s' % res)
