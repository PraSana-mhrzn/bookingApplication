from django.contrib.auth import views as auth_view
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path("register/",views.registerPage),
     path("logout/", auth_view.LogoutView.as_view(template_name="users/logout.html"), name="logout-page"),
     path("login/", auth_view.LoginView.as_view(template_name="users/login.html"), name="login-page"),
     path("profile/", views.profile)
]
