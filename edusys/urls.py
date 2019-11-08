from django.conf.urls import url
from django.urls import path

from edusys import views

urlpatterns = [
    path('', views.navbar),
    url(r'^register', views.enter_register, name='register'),
    path('signup', views.signup),
    path('login', views.login_form),
    path('login_page', views.login_page),
    path('contact_us', views.submit_contact),
    path('submit_contact', views.submit_contact),
    path('send_email', views.sendEmail),
    path('logout', views.logout_func),
    path('make_new_course',views.create_course),
    path('courses',views.courses),
    path('panel',views.panel)
]
