# coding=utf-8
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

# Create your views here.
from django.urls import path

from edusys.forms import SignUpForm, ContactUsForm


def navbar(request):
    return render(request, 'homepage.html', {'file': 'base.html', 'error': ''})\


def enter_register(request):
    return render(request, 'register.html')


def login_form(request):
    return render(request, 'login.html', {'error': ''})


def login_page(request):
    if request.method == 'POST':
        error = ""
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {'file': 'none.html', 'error': error}
            return render(request, 'homepage.html', context)
        else:
            error = "error"
            context = {'file': 'base.html', 'error': error}
            return render(request, 'login.html', context)
    else:
        login_form(request)


def signup(request):
    login_error = ''
    if request.method == "POST":
        form = SignUpForm(request.POST)
        pass2 = request.POST['password2']
        pass1 = request.POST['password1']
        if pass1 != pass2:
            login_error = 'گذرواژه و تکرار گذرواژه یکسان نیستند'
        if User.objects.filter(username__exact=request.POST['username']):
            login_error = 'نام کاربری شما در سیستم موجود است'
        if form.is_valid():
            user = form.save()
            user.save()
        # else:
    # return HttpResponse(login_error)
    return render(request, 'register.html', {"login_error": login_error})


def submit_contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("title")
            fromEmail = form.cleaned_data.get("email")
            body = str(form.cleaned_data.get("text")) + str(fromEmail)
            toEmail = "webe19lopers@gmail.com"
            # email = EmailMessage(subject, body, fromEmail, toEmail)
            # email.send()
            send_mail(subject, body, 'hamilamailee77@gmail.com', [toEmail])
            # email = EmailMessage(subject, body, 'hamilamailee77@gmail.com', [toEmail])
            # email.send()

            return render(request, 'contact_done.html')
        else:
            return render(request, 'contact_form.html')
    return render(request, 'contact_form.html')


def sendEmail(fromEmail, title, text):
    res = send_mail(title, (fromEmail, text), fromEmail, ['webe19lopers@gmail.com', ])
    return HttpResponse('%s' % res)