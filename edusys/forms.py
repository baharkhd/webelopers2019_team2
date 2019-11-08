from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class ContactUsForm(forms.Form):
    title = forms.CharField(max_length=200)
    email = forms.EmailField(required=True)
    text = forms.CharField(min_length=10, max_length=250, widget=forms.Textarea, required=True)


