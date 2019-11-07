from django.conf.urls import url
from django.urls import path

from edusys import views

urlpatterns = [
    path('', views.navbar),
    url(r'^register', views.enter_register, name='register'),
    path('signup', views.signup),
    path('login', views.login_form),
    path('login_page',views.login_page)

]
