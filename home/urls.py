from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.base, name='home'),
    path("base", views.base, name='base'),
    path("login", views.login_view, name='login'),
    path("signup", views.signup_views, name='signup'),
    path("computer_courses", views.computer_courses, name='computer_courses'),
    path("gate", views.gate, name='gate'),
    path("jee", views.jee, name='jee'),
    path("quiz", views.quiz, name='quiz'),
]