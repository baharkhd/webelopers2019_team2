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
    if request.user.is_authenticated:
        return render(request, 'homepage.html', {'file': 'none.html', 'error': ''})
    else:
        return render(request, 'homepage.html', {'file': 'base.html', 'error': ''})


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
            return redirect('/')
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


def logout_func(request):
    logout(request)
    return redirect('/')


def submit_contact(request):
    file = None
    if request.user.is_authenticated:
        file = 'none.html'
    else:
        file = 'base.html'
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("title")
            fromEmail = form.cleaned_data.get("email")
            body = str(form.cleaned_data.get("text")) + str(fromEmail)
            toEmail = "webe19lopers@gmail.com"
            print("subject:", subject)
            email = EmailMessage(subject, body, toEmail)
            email.send()
            return render(request, 'contact_done.html', {'file': file})
        else:
            return render(request, 'contact_form.html', {'file': file})
    return render(request, 'contact_form.html', {'file': file})


def sendEmail(fromEmail, title, text):
    res = send_mail(title, (fromEmail, text), fromEmail, ['webe19lopers@gmail.com', ])
    return HttpResponse('%s' % res)


def panel(request):
    return render(request, 'panel.html')


def create_course(request):
    return render(request, 'course_form.html')


def courses(request):
    return HttpResponse('courses')
