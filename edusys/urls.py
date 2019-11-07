from django.conf.urls import url
from django.urls import path

from edusys import views

urlpatterns = [
    path('', views.navbar),
    url(r'^register', views.enter_register, name='register'),
    path('signup', views.signup),
    path('login', views.enter_login),
    path('contact', views.enter_contact_page),
    path('user_login', views.user_login)

]
