from django.conf.urls import url
from django.urls import path

from edusys import views

urlpatterns = [
    path('', views.navbar),
    url(r'^register/', views.enter_register, name='register')
]
