
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.homepage), 
    
     path("about/",views.aboutPage),
     path("home/",views.homepage),
     path("myBookings/",views.myBookings),
     path("details/<int:id>",views.detailsPage),
]
