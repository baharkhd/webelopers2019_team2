from django.urls import path

from edusys import views

urlpatterns = [
    path('', views.navbar),
    path('homepage/', views.homepage)
]
